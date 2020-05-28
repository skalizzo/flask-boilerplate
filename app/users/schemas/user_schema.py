from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    nickname: str
    email: str
    password1: str
    password2: str


class CreateUserResponse(BaseModel):
    nickname: str
    email: str

    class Config:
        orm_mode = True
