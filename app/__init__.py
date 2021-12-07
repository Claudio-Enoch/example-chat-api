from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    from app.config import Config

    app.config.from_object(Config)

    # bootstrap app
    from app.models import Message, User

    db.init_app(app)

    from app.routes import api

    api.init_app(app)

    @app.shell_context_processor
    def shell_context():
        return dict(
            app=app,
            db=db,
            Message=Message,
            User=User,
        )

    return app
