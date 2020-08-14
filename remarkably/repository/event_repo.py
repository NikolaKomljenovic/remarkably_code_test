from repository import sqlalchemy_repo as sr


class EventRepo(sr.SqlAlchemyRepo):
    def save(self, event_data):
        return 0
