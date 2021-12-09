import docker
import pytest
from flask import Flask
from flask.testing import FlaskClient

from app import create_app, db
from db.health_check import check_postgres_connection
from tests.mocks import seed_db


@pytest.fixture(scope="function")
def app_client(app_context, _db_client) -> FlaskClient:
    yield app_context.test_client()


@pytest.fixture(scope="function")
def _db_client(app_context):
    db.drop_all()
    db.create_all()
    seed_db()
    yield db
    db.session.remove()


@pytest.fixture(scope="function", autouse=True)
def app_context(docker_postgres_connection_string, monkeypatch) -> Flask:
    monkeypatch.setenv("FLASK_ENV", "development")
    monkeypatch.setattr("app.config.Config.SQLALCHEMY_DATABASE_URI", docker_postgres_connection_string)
    app = create_app()
    with app.app_context():
        yield app


@pytest.fixture(scope="session", autouse=True)
def docker_postgres_connection_string() -> str:
    test_port = 5555
    connection_string = f"postgresql://postgres:postgres@localhost:{test_port}/warehouse"
    client = docker.from_env()
    image, logs = client.images.build(path="db")
    container = client.containers.run(image=image, ports={"5432/tcp": "5555"}, detach=True)
    try:
        check_postgres_connection(url=connection_string, tries=5)
        yield connection_string
    finally:
        container.stop()
