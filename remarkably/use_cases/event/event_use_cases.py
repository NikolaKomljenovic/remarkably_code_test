from repository.event_repo import EventRepo
from shared import response_object as res, use_case as uc
from shared.response_object import ResponseSuccess
from use_cases.event.event_request_objects import SaveEventRequestObject, GetEventRequestObject


class SaveEventUseCase(uc.UseCase):
    def __init__(self, repo: EventRepo):
        super().__init__()
        self.repo = repo

    def process_request(self, request_object: SaveEventRequestObject) -> ResponseSuccess:
        event = self.repo.save(event_data=request_object.data)
        return res.ResponseSuccess(event)


class GetEventsUseCase(uc.UseCase):
    def __init__(self, repo: EventRepo):
        super().__init__()
        self.repo = repo

    def process_request(self, request_object: GetEventRequestObject) -> ResponseSuccess:
        event = self.repo.get_all_events(filter_params=request_object.data)
        return res.ResponseSuccess(event)


class GetEventUseCase(uc.UseCase):
    def __init__(self, repo: EventRepo):
        super().__init__()
        self.repo = repo

    def process_request(self, request_object: GetEventRequestObject) -> ResponseSuccess:
        event = self.repo.get_event(event_id=request_object.data)
        return res.ResponseSuccess(event)


class GetTotalEventsByTypeUseCase(uc.UseCase):
    def __init__(self, repo: EventRepo):
        super().__init__()
        self.repo = repo

    def process_request(self, request_object: None) -> ResponseSuccess:
        event = self.repo.get_event_count_by_type()
        return res.ResponseSuccess(event)
