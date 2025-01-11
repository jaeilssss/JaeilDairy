from pydantic import BaseModel
from datetime import datetime
from src.common.function.password_util import hash_password
class SignUpModel(BaseModel):
    name: str
    email: str
    password: str
    phone_number: str
    birthday: str
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    
    def hashed_password(self):
       self.password = hash_password(self.password)