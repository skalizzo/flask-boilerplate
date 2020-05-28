from flask import Blueprint
from flask import request

from app.posts.schemas import (
    PostResponse,
    GetPostListRequest,
    GetPostListResponse,
    CreatePostRequest,
    UpdatePostRequest,
)
from app.posts.usecases import (
    GetPostListUsecase,
    CreatePostUsecase,
    GetPostUsecase,
    UpdatePostUsecase,
    DeletePostUsecase,
)
from core.parameters import parameters
from core.response import response
from core.utils import extract_user_id_from_header

post_bp = Blueprint('post', __name__)


@post_bp.route('', methods=['GET'])
@extract_user_id_from_header
@parameters(GetPostListRequest)
@response(GetPostListResponse)
def get_post_list(params: GetPostListRequest):
    return GetPostListUsecase().execute(prev=params.prev, limit=params.limit)


@post_bp.route('', methods=['POST'])
@extract_user_id_from_header
@parameters(CreatePostRequest)
@response(PostResponse)
def create_post(params: CreatePostRequest):
    return CreatePostUsecase().execute(
        user_id=request.user_id,
        caption=params.caption,
    )


@post_bp.route('/<int:post_id>/', methods=['GET'])
@extract_user_id_from_header
@response(PostResponse)
def get_post(post_id: int):
    return GetPostUsecase().execute(user_id=request.user_id, post_id=post_id)


@post_bp.route('/<int:post_id>/', methods=['PUT'])
@extract_user_id_from_header
@parameters(UpdatePostRequest)
@response(PostResponse)
def update_post(params: UpdatePostRequest, post_id: int):
    return UpdatePostUsecase().execute(
        user_id=request.user_id,
        post_id=post_id,
        caption=params.caption,
    )


@post_bp.route('/<int:post_id>/', methods=['DELETE'])
@extract_user_id_from_header
def delete_post(post_id: int):
    DeletePostUsecase().execute(user_id=request.user_id, post_id=post_id)
    return {'status': True}
