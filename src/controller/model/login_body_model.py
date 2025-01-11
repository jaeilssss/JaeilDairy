from pydantic import BaseModel
class LoginBodyModel(BaseModel):
    email: str
    password: str