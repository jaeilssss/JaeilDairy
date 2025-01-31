from abc import ABCMeta, abstractmethod
from src.service.model.user.logout_model import LogoutRequest
from src.service.model.find_my_user_info_model import FindMyUserInfoModel
from src.service.model.renew_token_model import RenewTokenModel
from src.service.model import SignUpModel
from src.service.model import LoginModel


class UserService(metaclass=ABCMeta):

    @abstractmethod
    async def create_user(self, sign_up_model: SignUpModel):
        pass

    @abstractmethod
    async def login(self, login_model: LoginModel):
        pass

    @abstractmethod
    async def renew_token(self, renew_token_model: RenewTokenModel):
        pass

    @abstractmethod
    async def get_my_user_info(self, find_my_user_info_model: FindMyUserInfoModel):
        pass

    @abstractmethod
    async def logout(self, logout_request: LogoutRequest):
        pass
