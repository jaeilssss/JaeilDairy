from pydantic import BaseModel
from datetime import datetime
class SignUpModel(BaseModel):
    name: str
    email: str
    password: str
    phone_number: str
    birthday: str
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()