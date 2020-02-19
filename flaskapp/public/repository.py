from . import models


class SqlAlchemyRepository:

    def __init__(self, session) -> None:
        self.session = session

    def add(self, user):
        self.session.add(user)
        return None

    def get(self, id):
        return self.session.query(models.User).filter_by(id=id).first()
