from os import environ

from flask.cli import FlaskGroup

from app import create_app
from app.config import Config

environ.setdefault("FLASK_ENV", "development")
Config.SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost:5432/warehouse"

if __name__ == "__main__":
    cli = FlaskGroup(create_app=create_app)
    cli()
