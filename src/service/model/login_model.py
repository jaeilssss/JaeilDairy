from pydantic import BaseModel


class LoginModel(BaseModel):
    email: str
    password: str


class LoginResponseModel(BaseModel):
    access_token: str
    refresh_token: str
