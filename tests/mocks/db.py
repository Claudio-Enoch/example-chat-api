from app.models import Message, User


def seed_db(db):
    user1 = User(username="UserOne")
    user2 = User(username="UserTwo")
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()
