from db import db
from sqlalchemy.dialects.postgresql import UUID

from shared.enum.type_enum import EventType


class Event(db.Model):
    __tablename__ = 'event'

    id = db.Column(UUID(as_uuid=True),
                   primary_key=True,
                   server_default=db.text("uuid_generate_v4()"))
    detail = db.Column(db.String(200), unique=False, nullable=False)
    type = db.Column(db.Enum(EventType), unique=False, nullable=False)
    created_date = db.Column(
        db.DateTime, default=db.func.now(), onupdate=db.func.now()
    )

