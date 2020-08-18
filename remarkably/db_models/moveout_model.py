from db import db

from sqlalchemy.dialects.postgresql import UUID


class MoveOut(db.Model):
    __tablename__ = 'moveout'

    id = db.Column(UUID(as_uuid=True),
                   primary_key=True,
                   server_default=db.text("uuid_generate_v4()"))
    created_date = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
    value = db.Column(db.Integer(), unique=False, nullable=False)
