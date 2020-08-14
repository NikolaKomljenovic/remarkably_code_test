from db import db


class SqlAlchemyRepo(object):

    def build_db_model(self, model_class, model_data):
        pass

    def save(self, db_object):
        db.session.add(db_object)

    def execute(self, query, parameters):
        return db.session.execute(query, parameters)

    @staticmethod
    def flush():
        db.session.flush()

    def save_list(self, db_object_list):
        for db_object in db_object_list:
            db.session.add(db_object)

    @staticmethod
    def commit():
        db.session.commit()

    @staticmethod
    def rollback():
        db.session.rollback()
