from abc import ABCMeta, abstractmethod
from src.common.entity.user.user_model import User
from src.repository.model import FindUserByEmailRequestModel


class UserRepository(metaclass=ABCMeta):

    @abstractmethod
    async def insert(self, user_model: User):
        pass

    @abstractmethod
    async def find_user_by_email(
        self, find_user_by_email_model: FindUserByEmailRequestModel
    ):
        pass

    @abstractmethod
    async def find_user_by_user_id(self, user_id: str):
        pass
