import collections
from typing import Dict, Union

from marshmallow import ValidationError

from mappers.event_mappers import CreateEventSchema
from shared import request_object as req
from shared.request_object import InvalidRequestObject


class SaveEventRequestObject(req.ValidRequestObject):
    def __init__(self, article_data: Dict[str, str]):
        self.data = article_data

    @classmethod
    def from_dict(cls, adict: Dict[str, str]) -> Union['SaveEventRequestObject', InvalidRequestObject]:
        global create_article
        invalid_req = req.InvalidRequestObject()

        if not isinstance(adict, collections.Mapping):
            invalid_req.add_error('article_data', 'is not iterable')

        try:
            create_article = CreateEventSchema().load(adict)
        except ValidationError as v_err:
            for param in v_err.messages:
                invalid_req.add_error(param, v_err.messages[param])

        if invalid_req.has_errors():
            return invalid_req

        return SaveEventRequestObject(create_article)
