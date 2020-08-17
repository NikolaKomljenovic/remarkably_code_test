from uuid import UUID

from flask import request
from flask_restplus import Namespace, Resource, fields

from mappers.event_mappers import EventResponseSchema, TotalByTypeResponseSchema
from repository.event_repo import EventRepo
from shared import response_object as res
from shared.enum.order_enum import OrderType

from use_cases.event import event_request_objects as req
from use_cases.event import event_use_cases as uc

api = Namespace('Event', description='Event endpoints for Remarkably Code Test')


STATUS_CODES = {
    res.ResponseSuccess.SUCCESS: 200,
    res.ResponseFailure.RESOURCE_ERROR: 404,
    res.ResponseFailure.PARAMETERS_ERROR: 400,
    res.ResponseFailure.BUSINESS_ERROR: 400,
    res.ResponseFailure.SYSTEM_ERROR: 500
}

# SWAGGER DOC
event_model = api.model('Event model', {
    'item': fields.String(description='event id'),
    'detail': fields.String(description='Details about event'),
    'type': fields.String(description='Type of an event'),
    'created': fields.DateTime(description='Date of event creation')
})

create_event_model = api.model('Create event model', {
    'detail': fields.String(description='Details about event'),
    'type': fields.String(description='Type of an event'),
})

event_total_by_type_model = api.model('Total events by type model', {
    'system': fields.Integer(description='System event total'),
    'external': fields.Integer(description='External event total'),
    'staff': fields.Integer(description='Staff event total'),
    'user': fields.Integer(description='User event total'),
    'unknown': fields.Integer(description='Unknown event total')
})


@api.route('')
class Event(Resource):
    @api.response(200, 'Success', event_model)
    @api.response(404, 'Resource error')
    @api.response(400, 'Parameters error')
    @api.response(500, 'System error')
    @api.expect(create_event_model)
    # POST new event into database
    def post(self):
        # Get event data
        event = request.get_json()

        request_object = req.SaveEventRequestObject.from_dict(adict=event)

        use_case = uc.SaveEventUseCase(EventRepo())

        response = use_case.execute(request_object)

        if not response:
            api.abort(STATUS_CODES[response.type],
                      response.message,
                      error_code=response.error_code,
                      error_key=response.error_key,
                      error_params=response.error_params)

        result = EventResponseSchema().dump(response.value)

        return result

    def get(self):
        filter_params = {
            'sort': request.args.get('sort', default=OrderType.DESCENDING, type=OrderType)
        }

        request_object = req.GetEventsRequestObject.from_filter_list(filter_params)

        use_case = uc.GetEventsUseCase(EventRepo())

        response = use_case.execute(request_object)

        if not response:
            api.abort(STATUS_CODES[response.type],
                      response.message,
                      error_code=response.error_code,
                      error_key=response.error_key,
                      error_params=response.error_params)

        result = EventResponseSchema(many=True).dump(response.value)

        return result


@api.route('/<string:uuid>')
class SpecificEvent(Resource):
    @api.response(200, 'Success', event_model)
    @api.response(404, 'Resource error')
    @api.response(400, 'Parameters error')
    @api.response(500, 'System error')
    # GET specific event from database
    def get(self, uuid):
        try:
            uuid = UUID(uuid)
        except ValueError:
            return api.abort(400, 'Wrong input data provided')

        request_object = req.GetEventRequestObject.from_uuid(uuid=uuid)

        use_case = uc.GetEventUseCase(EventRepo())

        response = use_case.execute(request_object)

        if not response:
            api.abort(STATUS_CODES[response.type],
                      response.message,
                      error_code=response.error_code,
                      error_key=response.error_key,
                      error_params=response.error_params)

        result = EventResponseSchema().dump(response.value)

        return result


@api.route('/totalbytype')
class SpecificEvent(Resource):
    @api.response(200, 'Success', event_total_by_type_model)
    @api.response(404, 'Resource error')
    @api.response(400, 'Parameters error')
    @api.response(500, 'System error')
    # GET count of events by type from database
    def get(self):
        use_case = uc.GetTotalEventsByTypeUseCase(EventRepo())

        response = use_case.execute()

        if not response:
            api.abort(STATUS_CODES[response.type],
                      response.message,
                      error_code=response.error_code,
                      error_key=response.error_key,
                      error_params=response.error_params)

        result = TotalByTypeResponseSchema().dump(response.value)

        return result


@api.route('/oldestevent')
class SpecificEvent(Resource):
    @api.response(200, 'Success', event_model)
    @api.response(404, 'Resource error')
    @api.response(400, 'Parameters error')
    @api.response(500, 'System error')
    # GET oldest event from database
    def get(self):
        use_case = uc.OldestEventUseCase(EventRepo())

        response = use_case.execute()

        if not response:
            api.abort(STATUS_CODES[response.type],
                      response.message,
                      error_code=response.error_code,
                      error_key=response.error_key,
                      error_params=response.error_params)

        result = EventResponseSchema().dump(response.value)

        return result


@api.route('/newestevent')
class SpecificEvent(Resource):
    @api.response(200, 'Success', event_model)
    @api.response(404, 'Resource error')
    @api.response(400, 'Parameters error')
    @api.response(500, 'System error')
    # GET newest event from database
    def get(self):
        use_case = uc.NewestEventUseCase(EventRepo())

        response = use_case.execute()

        if not response:
            api.abort(STATUS_CODES[response.type],
                      response.message,
                      error_code=response.error_code,
                      error_key=response.error_key,
                      error_params=response.error_params)

        result = EventResponseSchema().dump(response.value)

        return result