from sqlalchemy import (Column, BigInteger, Unicode)

from core.db import Base
from core.db.mixin import TimestampMixin


class User(Base, TimestampMixin):
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nickname = Column(Unicode(length=20), unique=True, nullable=False)
    email = Column(Unicode(length=100), unique=True, nullable=False)
    password = Column(Unicode(length=100), nullable=False)
