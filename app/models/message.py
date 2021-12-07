from dataclasses import dataclass

from app import db


@dataclass
class Message(db.Model):
    __table_args__ = {"schema": "chat"}

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("chat.user.id"))
    recipient_id = db.Column(db.Integer, db.ForeignKey("chat.user.id"))

    author = db.relationship("User", foreign_keys=[author_id], backref="messages_sent")
    recipient = db.relationship("User", foreign_keys=[recipient_id], backref="messages_received")
