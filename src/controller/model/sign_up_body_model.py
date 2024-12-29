from pydantic import BaseModel
class SignUpBodymodel(BaseModel):
    name: str
    email: str
    password: str
    phone_number: str
    birthday: str