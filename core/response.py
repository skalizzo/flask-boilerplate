from functools import wraps

from flask import jsonify
from pydantic import BaseModel

from core.exceptions import CustomException


def response(schema):
    """
    Return response using given pydantic schema
    """
    def _response(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if issubclass(schema, BaseModel):
                has_root = True if '__root__' in schema.__fields__ else False
                function_res = function(*args, **kwargs)

                if not function_res:
                    if has_root is True:
                        return jsonify([])
                    return jsonify({})

                if type(function_res) == list:
                    res = schema.parse_obj(function_res)
                else:
                    res = schema.from_orm(function_res)

                res = res.dict()

                if has_root is True:
                    return jsonify(res['__root__'])

                return jsonify(res)
            elif isinstance(schema, dict):
                return jsonify(schema)
            else:
                raise CustomException('invalid response type', code=400)

        return wrapper
    return _response
