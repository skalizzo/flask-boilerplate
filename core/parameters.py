from functools import wraps

from flask import request
from pydantic import BaseModel, ValidationError

from core.exceptions import CustomException


def parameters(schema):
    """
    Validate query parameters or request body and inject it through function argument
    """
    def _parameters(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if not issubclass(schema, BaseModel):
                raise CustomException('invalid schema', code=400)

            if request.method == 'GET':
                params = dict(request.args)
            else:
                params = request.get_json(force=True)

            try:
                serialized_data = schema(**params)
            except ValidationError as e:
                raise CustomException(str(e), code=422)

            return function(serialized_data, *args, **kwargs)
        return wrapper
    return _parameters
