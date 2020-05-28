from flask import Blueprint

from app.users.schemas import CreateUserRequest, CreateUserResponse
from app.users.usecases import CreateUserUsecase
from core.parameters import parameters
from core.response import response

user_bp = Blueprint('user', __name__)


@user_bp.route('', methods=['POST'])
@parameters(CreateUserRequest)
@response(CreateUserResponse)
def create_user(params: CreateUserRequest):
    return CreateUserUsecase().execute(
        nickname=params.nickname,
        email=params.email,
        password1=params.password1,
        password2=params.password2,
    )
