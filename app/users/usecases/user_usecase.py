from typing import Union, NoReturn

import bcrypt
from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError

from app.users.models import User
from core.db import session
from core.exceptions import CustomException


class UserUsecase:
    def _is_exist(self, nickname: str = None, email: str = None) -> bool:
        query = session.query(User)

        if nickname:
            query = query.filter(User.nickname == nickname)

        if email:
            query = query.filter(User.email == email)

        return query.first() is not None


class CreateUserUsecase(UserUsecase):
    def execute(
        self,
        nickname: str,
        email: str,
        password1: str,
        password2: str,
    ) -> Union[User, NoReturn]:
        if password1 != password2:
            raise CustomException('password1, 2 does not match', code=400)

        if self._is_exist(nickname=nickname, email=email):
            raise CustomException('already exists', 400)

        password = bcrypt.hashpw(
            password=password1.encode('utf-8'),
            salt=bcrypt.gensalt(),
        )

        user = User(nickname=nickname, email=email, password=password)

        try:
            session.add(user)
            session.commit()
        except IntegrityError as e:
            session.rollback()
            raise CustomException(str(e), code=500)

        return user
