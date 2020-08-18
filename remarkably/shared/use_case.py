from exceptions.api_exceptions import BusinessException, ParameterException, ResourceException
from shared import response_object as res


class UseCase(object):

    def execute(self, request_object=None):
        try:
            result = self.process_request(request_object)
            return result
        except ResourceException as rex:
            return res.ResponseFailure.build_resource_error(str(rex), rex.error_code, rex.error_key, rex.error_params)

        except ParameterException as pex:
            return res.ResponseFailure.build_parameters_error(str(pex), pex.error_code, pex.error_key, pex.error_params)

        except BusinessException as bex:
            return res.ResponseFailure.build_business_error(str(bex), bex.error_code, bex.error_key, bex.error_params)

        except Exception as exc:
            return res.ResponseFailure.build_system_error(str(exc), 0, '_unhandled_error')

    def process_request(self, request_object):
        raise NotImplementedError(
            "process_request() not implemented by UseCase class")
