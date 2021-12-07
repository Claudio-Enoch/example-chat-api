from dataclasses import dataclass

from app import db


@dataclass
class User(db.Model):
    __table_args__ = {"schema": "chat"}

    id: int = db.Column(db.Integer, primary_key=True)
    username: str = db.Column(db.String, unique=True, nullable=False)
