from app import db


class CRUD:
    def __init__(self, **kwargs):
        [setattr(self, k, v) for k, v in kwargs.items()]

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self, **kwargs):
        [setattr(self, k, v) for k, v in kwargs.items()]
        db.session.commit()
        return self
