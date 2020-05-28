from app.users.models import User
from app.users.usecases import CreateUserUsecase


def test_create_user_usecase():
    user = CreateUserUsecase().execute(
        nickname='test',
        email='test@test.com',
        password1='test123',
        password2='test123',
    )

    assert isinstance(user, User)
    assert user.nickname == 'test'
    assert user.email == 'test@test.com'
    assert user.password != 'test123'
    assert user.password != 'test123'
