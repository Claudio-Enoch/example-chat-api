from datetime import datetime, timedelta

from app.models import Message, User


def seed_db():
    User(username="DefaultUser").create()
    User(username="OutdatedMessages").create()
    User(username="OnlyRecipient").create()
    User(username="OnlyAuthor").create()
    User(username="NoMessagesReceived").create()
    User(username="150MessagesReceived").create()

    delta_35_days = datetime.utcnow() - timedelta(days=35)
    for _ in range(150):
        Message(content="M", author_id=1, recipient_id=6).create()
    Message(content="Hello World", author_id=1, recipient_id=3).create()
    Message(content="To OnlyRecipient User", author_id=1, recipient_id=3).create()
    Message(content="To OutdatedMessages User", author_id=1, recipient_id=2, created_date=delta_35_days).create()
    Message(content="From OnlyAuthor", author_id=4, recipient_id=1).create()
