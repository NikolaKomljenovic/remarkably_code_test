from db_models.event_model import Event
from mappers.event_mappers import EventResponseSchema, TotalByTypeResponseSchema
from repository import sqlalchemy_repo as sr


class EventRepo(sr.SqlAlchemyRepo):
    def save(self, event_data):
        event_data.commit()
        return EventResponseSchema().dump(event_data)

    def get_all_events(self, filter_params):
        all_events = Event.find_all_events(filter_params)
        return EventResponseSchema(many=True).dump(all_events)

    def get_event(self, event_id):
        event = Event.find_by_id(event_id=event_id)
        return EventResponseSchema().dump(event)

    def get_event_count_by_type(self):
        event_by_type = Event.find_total_by_type()
        return TotalByTypeResponseSchema().dump(event_by_type)

    def oldest_event(self):
        oldest_event = Event.find_oldest_event()
        return EventResponseSchema().dump(oldest_event)

    def newest_event(self):
        newest_event = Event.find_newest_event()
        return EventResponseSchema().dump(newest_event)
