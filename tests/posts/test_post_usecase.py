from app.posts.models import Post
from app.posts.usecases import (
    GetPostListUsecase,
    CreatePostUsecase,
    GetPostUsecase,
    UpdatePostUsecase,
    DeletePostUsecase,
)


def test_get_post_list_usecase():
    posts = GetPostListUsecase().execute(user_id=1, limit=10)

    assert type(posts) == list
    assert isinstance(posts[0], Post)


def test_create_post_usecase():
    post = CreatePostUsecase().execute(user_id=1, caption='test caption')

    assert isinstance(post, Post)
    assert post.id == 1
    assert post.caption == 'test caption'


def test_get_post_usecase():
    post = GetPostUsecase().execute(user_id=1, post_id=1)

    assert isinstance(post, Post)
    assert post.id == 1


def test_update_post_usecase():
    post = UpdatePostUsecase().execute(
        user_id=1,
        post_id=1,
        caption='update caption',
    )

    assert isinstance(post, Post)
    assert post.id == 1
    assert post.user_id == 1
    assert post.caption == 'update caption'


def test_delete_post_usecase():
    post = DeletePostUsecase().execute(user_id=1, post_id=1)

    assert post is True
