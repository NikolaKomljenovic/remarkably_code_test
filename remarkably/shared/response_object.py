class ResponseSuccess(object):
    SUCCESS = 'SUCCESS'

    def __init__(self, value=None):
        self.type = self.SUCCESS
        self.value = value

    def __nonzero__(self):
        return True

    __bool__ = __nonzero__


class ResponseFailure(object):
    RESOURCE_ERROR = 'RESOURCE_ERROR'
    PARAMETERS_ERROR = 'PARAMETERS_ERROR'
    SYSTEM_ERROR = 'SYSTEM_ERROR'
    BUSINESS_ERROR = 'BUSINESS_ERROR'

    def __init__(self, type_, message, error_code=0, error_key='', error_params={}, inner_error_message=''):
        self.type = type_
        self.message = self._format_message(message)
        self.error_code = error_code
        self.error_key = error_key
        self.error_params = error_params
        self.inner_error_message = inner_error_message

    def _format_message(self, msg):
        if isinstance(msg, Exception):
            return "{}: {}".format(msg.__class__.__name__, "{}".format(msg))
        return msg

    @property
    def value(self):
        return {'type': self.type, 'message': self.message}

    def __bool__(self):
        return False

    @classmethod
    def build_resource_error(cls, message=None, error_code=None, error_key=None, error_params={}, inner_error_message=''):
        return cls(cls.RESOURCE_ERROR, message, error_code, error_key, error_params, inner_error_message)

    @classmethod
    def build_system_error(cls, message=None, error_code=None, error_key=None, error_params={}, inner_error_message=''):
        return cls(cls.SYSTEM_ERROR, message, error_code, error_key, error_params, inner_error_message)

    @classmethod
    def build_parameters_error(cls, message=None, error_code=None, error_key=None, error_params={}, inner_error_message=''):
        return cls(cls.PARAMETERS_ERROR, message, error_code, error_key, error_params, inner_error_message)

    @classmethod
    def build_business_error(cls, message=None, error_code=None, error_key=None, error_params={}, inner_error_message=''):
        return cls(cls.BUSINESS_ERROR, message, error_code, error_key, error_params, inner_error_message)

    @classmethod
    def build_from_invalid_request_object(cls, invalid_request_object):
        message = "\n".join(["{}: {}".format(err['parameter'], err['message'])
                             for err in invalid_request_object.errors])
        return cls.build_parameters_error(message)
