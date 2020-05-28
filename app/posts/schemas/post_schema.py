from typing import List
from typing import Optional

from core.base_orm_model import BaseOrmModel


class NestedComment(BaseOrmModel):
    id: int
    user_id: int
    body: str


class PostResponse(BaseOrmModel):
    id: int
    user_id: int
    caption: str
    comments: List[NestedComment]

    class Config:
        orm_mode = True


class GetPostListRequest(BaseOrmModel):
    prev: Optional[int] = None
    limit: Optional[int] = 10

    class Config:
        orm_mode = True


class GetPostListResponse(BaseOrmModel):
    __root__: List[PostResponse]


class CreatePostRequest(BaseOrmModel):
    caption: str


class UpdatePostRequest(BaseOrmModel):
    caption: str
