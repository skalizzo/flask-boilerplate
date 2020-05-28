from sqlalchemy import (Column, BigInteger, Unicode, ForeignKey)
from sqlalchemy.orm import relationship

from core.db import Base
from core.db.mixin import TimestampMixin


class Post(Base, TimestampMixin):
    __tablename__ = 'posts'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(ForeignKey('users.id'), nullable=False)
    caption = Column(Unicode(length=255), nullable=True)
    comments = relationship('Comment')


class Comment(Base, TimestampMixin):
    __tablename__ = 'comments'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    post_id = Column(ForeignKey('posts.id'), nullable=False)
    body = Column(Unicode(length=255), nullable=False)
    user_id = Column(ForeignKey('users.id'), nullable=False)
    parent_id = Column(ForeignKey('comments.id'), nullable=True)
