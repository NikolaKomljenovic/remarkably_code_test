from marshmallow import Schema, fields


class CreateEventSchema(Schema):
    id = fields.UUID(dump_only=True)
    title = fields.Str(dump_only=True)
    content = fields.Str(dump_only=True)
    preview = fields.Str(dump_only=True)


class EventResponseSchema(Schema):
    id = fields.UUID(dump_only=True)
    title = fields.Str(dump_only=True)
    content = fields.Str(dump_only=True)
    preview = fields.Str(dump_only=True)
