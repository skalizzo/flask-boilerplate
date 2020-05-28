from datetime import datetime, timedelta
from typing import Union, NoReturn

import jwt

from core.config import get_config
from core.exceptions import CustomException


class TokenHelper:
    TOKEN_EXPIRE_PERIOD = 604800
    REFRESH_TOKEN_EXPIRE_PERIOD = 1209600

    def __init__(self):
        self.config = get_config()

    def encode(
        self,
        payload: dict,
        expire_period: int = TOKEN_EXPIRE_PERIOD,
    ) -> str:
        token = jwt.encode(
            payload={
                **payload,
                'exp': datetime.utcnow() + timedelta(seconds=expire_period),
            },
            key=self.config.jwt_secret_key,
            algorithm=self.config.jwt_algorithm,
        ).decode('utf8')
        return token

    def decode(self, token: str) -> Union[dict, NoReturn]:
        try:
            return jwt.decode(
                token,
                self.config.jwt_secret_key,
                self.config.jwt_algorithm,
            )
        except jwt.exceptions.DecodeError:
            raise CustomException('invalid token', code=401)
        except jwt.exceptions.ExpiredSignatureError:
            raise CustomException('token expired', code=401)

    def decode_expired_token(self, token: str) -> Union[dict, NoReturn]:
        try:
            return jwt.decode(
                token,
                self.config.jwt_secret_key,
                self.config.jwt_algorithm,
                options={'verify_exp': False}
            )
        except jwt.exceptions.DecodeError:
            raise CustomException('invalid token', code=401)
