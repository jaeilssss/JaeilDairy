from abc import ABCMeta, abstractmethod
from src.service.model import SignUpModel

class UserService(metaclass = ABCMeta):
    
    @abstractmethod
    async def create_user(self, sign_up_model: SignUpModel):
        pass