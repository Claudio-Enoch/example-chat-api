from dataclasses import dataclass

from app import db
from app.models.crud import CRUD


@dataclass
class User(db.Model, CRUD):
    __table_args__ = {"schema": "chat"}

    id: int = db.Column(db.Integer, primary_key=True)
    username: str = db.Column(db.String, unique=True, nullable=False)
