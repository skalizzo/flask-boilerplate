from typing import Union, NoReturn

from sqlalchemy.exc import IntegrityError

from app.posts.models import Post
from core.db import session
from core.exceptions import CustomException


class PostUsecase:
    def __init__(self):
        pass


class GetPostListUsecase(PostUsecase):
    def execute(self, prev: int, limit: int = 10):
        query = session.query(Post)

        if prev:
            query = query.filter(Post.id < prev)

        return query.order_by(Post.id.desc()).limit(limit).all()


class CreatePostUsecase(PostUsecase):
    def execute(self, user_id: int, caption: str) -> Union[Post, NoReturn]:
        post = Post(user_id=user_id, caption=caption)

        try:
            session.add(post)
            session.commit()
        except IntegrityError as e:
            session.rollback()
            raise CustomException(str(e), code=500)

        return post


class GetPostUsecase(PostUsecase):
    def execute(self, user_id: int, post_id: int) -> Union[Post, NoReturn]:
        post = session.query(Post).filter(
            Post.id == post_id,
            Post.user_id == user_id,
        ).first()

        return post


class UpdatePostUsecase(PostUsecase):
    def execute(
        self,
        user_id: int,
        post_id: int,
        caption: str,
    ) -> Union[Post, NoReturn]:
        post = session.query(Post).filter(
            Post.id == post_id,
            Post.user_id == user_id,
        ).first()

        if not post:
            raise CustomException('post not found', code=404)

        post.caption = caption

        try:
            session.add(post)
            session.commit()
        except IntegrityError as e:
            session.rollback()
            raise CustomException(str(e), code=500)

        return post


class DeletePostUsecase(PostUsecase):
    def execute(self, user_id: int, post_id: int) -> Union[bool, NoReturn]:
        post = session.query(Post).filter(Post.id == post_id).first()

        if post.user_id != user_id:
            raise CustomException('do not have permission', code=401)

        try:
            session.delete(post)
            session.commit()
        except IntegrityError as e:
            raise CustomException(str(e), code=500)

        return True
