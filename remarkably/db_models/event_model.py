from db import db
from sqlalchemy.dialects.postgresql import UUID

from shared.enum.order_enum import OrderType
from shared.enum.type_enum import EventType


class Event(db.Model):
    __tablename__ = 'event'

    id = db.Column(UUID(as_uuid=True),
                   primary_key=True,
                   server_default=db.text("uuid_generate_v4()"))
    detail = db.Column(db.String(200), unique=False, nullable=False)
    type = db.Column(db.Enum(EventType), unique=False, nullable=False)
    created_date = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    @classmethod
    def find_by_id(cls, event_id):
        return cls.query.filter_by(id=event_id).first()

    @classmethod
    def find_total_by_type(cls):
        return {
            'unknown': cls.query.filter_by(type=EventType.UNKNOWN).count(),
            'external': cls.query.filter_by(type=EventType.EXTERNAL).count(),
            'staff': cls.query.filter_by(type=EventType.STAFF).count(),
            'user': cls.query.filter_by(type=EventType.USER).count(),
            'system': cls.query.filter_by(type=EventType.SYSTEM).count()
        }

    @classmethod
    def find_all_events(cls, filter_params):
        query = cls.query

        if filter_params['sort'] == OrderType.ASCENDING:
            query = query.order_by(cls.created_date.asc())
        elif filter_params['sort'] == OrderType.DESCENDING:
            query = query.order_by(cls.created_date.desc())

        return query.all()

    def commit(self):
        db.session.add(self)
        db.session.commit()

    def remove(self):
        db.session.delete(self)
        db.session.commit()
