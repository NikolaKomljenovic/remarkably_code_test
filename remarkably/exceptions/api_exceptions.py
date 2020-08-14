class ResourceException(Exception):
    ERROR_CODE = 20
    ERROR_KEY = '_resource_exception'
    ERROR_MESSAGE = 'Resource exception'
    ERROR_PARAMS_KEYS = []

    def __init__(self, error_message=ERROR_MESSAGE, error_code=ERROR_CODE, error_key=ERROR_KEY, error_param_keys=ERROR_PARAMS_KEYS, error_param_values=[]):
        super().__init__(error_message.format(*error_param_values))
        self.error_code = error_code
        self.error_key = error_key
        self.error_params = dict(zip(error_param_keys, error_param_values))


class ResourceNotFoundException(ResourceException):
    ERROR_CODE = 21
    ERROR_KEY = '_resource_not_found'
    ERROR_MESSAGE = 'Resource not found exception'
    ERROR_PARAMS_KEYS = []

    def __init__(self, error_message=ERROR_MESSAGE, error_code=ERROR_CODE, error_key=ERROR_KEY, error_param_keys=ERROR_PARAMS_KEYS, error_param_values=[]):
        super().__init__(error_message, error_code, error_key, error_param_keys, error_param_values)


class ParameterException(Exception):
    ERROR_CODE = 30
    ERROR_KEY = '_param_exception'
    ERROR_MESSAGE = 'Parameter exception'
    ERROR_PARAMS_KEYS = []

    def __init__(self, error_message=ERROR_MESSAGE, error_code=ERROR_CODE, error_key=ERROR_KEY, error_param_keys=ERROR_PARAMS_KEYS, error_param_values=[]):
        super().__init__(error_message.format(*error_param_values))
        self.error_code = error_code
        self.error_key = error_key
        self.error_params = dict(zip(error_param_keys, error_param_values))


class ParameterNotFoundException(ParameterException):
    ERROR_CODE = 31
    ERROR_KEY = '_param_not_found'
    ERROR_MESSAGE = 'Parameter {} not found exception'
    ERROR_PARAMS_KEYS = ['param_value']

    def __init__(self, error_message=ERROR_MESSAGE, error_code=ERROR_CODE, error_key=ERROR_KEY, error_param_keys=ERROR_PARAMS_KEYS, error_param_values=[]):
        super().__init__(error_message, error_code, error_key, error_param_keys, error_param_values)


class ParameterWrongValueException(ParameterException):
    ERROR_CODE = 32
    ERROR_KEY = '_param_wrong_value'
    ERROR_MESSAGE = 'Parameter wrong value exception'
    ERROR_PARAMS_KEYS = ['param_value']

    def __init__(self, error_message=ERROR_MESSAGE, error_code=ERROR_CODE, error_key=ERROR_KEY, error_param_keys=ERROR_PARAMS_KEYS, error_param_values=[]):
        super().__init__(error_message, error_code, error_key, error_param_keys, error_param_values)


class BusinessException(Exception):
    ERROR_CODE = 40
    ERROR_KEY = '_business_exception'
    ERROR_MESSAGE = 'Business exception'
    ERROR_PARAMS_KEYS = []

    def __init__(self, error_message=ERROR_MESSAGE, error_code=ERROR_CODE, error_key=ERROR_KEY, error_param_keys=ERROR_PARAMS_KEYS, error_param_values=[]):
        super().__init__(error_message.format(*error_param_values))
        self.error_code = error_code
        self.error_key = error_key
        self.error_params = dict(zip(error_param_keys, error_param_values))


class ActionNotAllowedException(BusinessException):
    ERROR_CODE = 41
    ERROR_KEY = '_action_not_allowed'
    ERROR_MESSAGE = 'Action not allowed'
    ERROR_PARAMS_KEYS = []

    def __init__(self, error_message=ERROR_MESSAGE, error_code=ERROR_CODE, error_key=ERROR_KEY, error_param_keys=ERROR_PARAMS_KEYS, error_param_values=[]):
        super().__init__(error_message, error_code, error_key, error_param_keys, error_param_values)