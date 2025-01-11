from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from src.common.function.password_util import verify_password
Base = declarative_base()
class UserModel(Base):
    __tablename__  = "user"
    
    id = Column(Integer, primary_key=True, autoincrement= True, name= "user_id")
    name= Column(String, nullable=False)
    email= Column(String, nullable=False)
    birthday= Column(String(11), nullable=False)
    password= Column(String, nullable=False)
    phone_number = Column(String)
    created_at= Column(DateTime)
    updated_at= Column(DateTime)
    

    def validation_password(self, password: str):
        print(self.password)
        print(password)
        return verify_password(password, self.password) 