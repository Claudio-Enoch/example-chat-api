from os import environ

from flask.cli import FlaskGroup

from app import create_app, db
from tests.mocks import seed_db
from app.config import Config

environ.setdefault("FLASK_ENV", "development")
DEFAULT_URI = "postgresql://postgres:postgres@localhost:5432/warehouse"
Config.SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI", DEFAULT_URI)

cli = FlaskGroup(create_app=create_app)


@cli.command("seed_db")
def seed():
    db.drop_all()
    db.create_all()
    seed_db()
    db.session.commit()


if __name__ == "__main__":
    cli()
