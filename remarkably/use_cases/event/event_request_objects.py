import collections
from abc import ABC
from typing import Dict, Union
from uuid import UUID

from marshmallow import ValidationError

from mappers.event_mappers import CreateEventSchema
from shared import request_object as req
from shared.request_object import InvalidRequestObject


class SaveEventRequestObject(req.ValidRequestObject):
    def __init__(self, event_data: Dict[str, str]):
        self.data = event_data

    @classmethod
    def from_dict(cls, adict: Dict[str, str]) -> Union['SaveEventRequestObject', InvalidRequestObject]:
        global create_event
        invalid_req = req.InvalidRequestObject()

        if not isinstance(adict, collections.Mapping):
            invalid_req.add_error('event_data', 'is not iterable')

        try:
            create_event = CreateEventSchema().load(adict)
        except ValidationError as v_err:
            for param in v_err.messages:
                invalid_req.add_error(param, v_err.messages[param])

        if invalid_req.has_errors():
            return invalid_req

        return SaveEventRequestObject(create_event)


class GetEventsRequestObject(req.ValidRequestObject, ABC):
    def __init__(self, event_data: Dict[str, str]):
        self.data = event_data

    @classmethod
    def from_filter_list(cls, filter_params: Dict[str, str]) -> 'GetEventsRequestObject':
        return GetEventsRequestObject(filter_params)


class GetEventRequestObject(req.ValidRequestObject, ABC):
    def __init__(self, uuid: UUID):
        self.data = uuid

    @classmethod
    def from_uuid(cls, uuid: UUID) -> 'GetEventRequestObject':
        return GetEventRequestObject(uuid)


class GetEventForSpecificItemRequestObject(req.ValidRequestObject, ABC):
    def __init__(self, uuid: UUID):
        self.data = uuid

    @classmethod
    def from_uuid(cls, uuid: UUID) -> 'GetEventForSpecificItemRequestObject':
        return GetEventForSpecificItemRequestObject(uuid)
