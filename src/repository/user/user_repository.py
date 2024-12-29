from abc import ABCMeta, abstractmethod
from src.common.entity.user import UserModel
class UserRepository(metaclass= ABCMeta):
    
    @abstractmethod
    async def insert(self, user_model: UserModel):
        pass