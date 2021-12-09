import datetime
from dataclasses import dataclass

from app import db
from app.models.crud import CRUD


@dataclass
class Message(db.Model, CRUD):
    __table_args__ = {"schema": "chat"}

    id: int = db.Column(db.Integer, primary_key=True)
    author_id: int = db.Column(db.Integer, db.ForeignKey("chat.user.id"))
    recipient_id: int = db.Column(db.Integer, db.ForeignKey("chat.user.id"))
    content: str = db.Column(db.Text, nullable=False)
    created_date: datetime.datetime = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    author = db.relationship("User", foreign_keys=[author_id], backref="messages_sent")
    recipient = db.relationship("User", foreign_keys=[recipient_id], backref="messages_received")
