from marshmallow import Schema, fields, post_load

from db_models.event_model import Event


class CreateEventSchema(Schema):
    type = fields.Str()
    detail = fields.Str()

    @post_load
    def make_event(self, data, **kwargs):
        return Event(**data)


class EventResponseSchema(Schema):
    id = fields.UUID(dump_only=True)
    type = fields.Str(dump_only=True)
    detail = fields.Str(dump_only=True)
    created_date = fields.Str(dump_only=True)
