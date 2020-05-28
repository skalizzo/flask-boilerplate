from functools import wraps

from flask import request

from core.exceptions import CustomException
from .token_helper import TokenHelper


def extract_user_id_from_header(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        try:
            token = request.headers['Authorization'].split()[1]
        except KeyError:
            raise CustomException('invalid authorize header', code=401)

        try:
            payload = TokenHelper().decode(token=token)
        except (AttributeError, KeyError):
            raise CustomException('authorize error', code=401)

        request.user_id = payload['user_id']
        return function(*args, **kwargs)

    return wrapper
