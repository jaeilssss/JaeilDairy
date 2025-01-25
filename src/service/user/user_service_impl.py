import os
from src.service.model.find_my_user_info_model import (
    FindMyUserInfoModel,
    FindMyUserInfoResponseModel,
)
from src.service.model.renew_token_model import RenewTokenModel
from src.service.user import UserService
from src.service.model import SignUpModel, LoginModel, LoginResponseModel
from src.repository.user import UserRepository
from src.common.entity.user.user_model import User
from src.common.exception.user_exception import (
    NotFoundUserError,
    ValidationEmailError,
    UserNotFoundError,
)
from src.repository.model.find_user_by_email_request_model import (
    FindUserByEmailRequestModel,
)
from src.common.function.jwt import AbstractJWTDecoder, AbstractJWTEncoder


class UserServiceImpl(UserService):
    def __init__(
        self,
        user_repository: UserRepository,
        jwt_encoder: AbstractJWTEncoder,
        jwt_decoder: AbstractJWTDecoder,
    ):
        self.user_repo = user_repository
        self.jwt_encoder = jwt_encoder
        self.jwt_decoder = jwt_decoder
        self.secret_key = os.getenv("JWT_SECRET_KEY")
        self.algorithm = os.getenv("JWT_ALGORITHM")
        self.ACCESS_TOKEN_EXPIRE_MINUTES = 30
        self.REFRESH_TOKEN_EXPIRE_MINUTES = 600 * 24 * 7

    async def create_user(self, sign_up_model: SignUpModel):
        sign_up_model.hashed_password()
        user = await self.user_repo.find_user_by_email(
            FindUserByEmailRequestModel(email=sign_up_model.email)
        )
        if user is not None:
            raise ValidationEmailError

        await self.user_repo.insert(user_model=User(**sign_up_model.model_dump()))

    async def login(self, login_model: LoginModel):
        user = await self.user_repo.find_user_by_email(
            FindUserByEmailRequestModel(email=login_model.email)
        )
        if user is None:
            raise UserNotFoundError

        if not user.validation_password(login_model.password):
            raise UserNotFoundError

        return self.__generate_token(user)

    async def renew_token(self, renew_token_model: RenewTokenModel):
        payload = self.jwt_decoder.decode(renew_token_model.refresh_token)
        user_id = payload.get("user_id")
        if user_id is None:
            pass
        user = await self.user_repo.find_user_by_user_id(user_id)
        return self.__generate_token(user)

    async def get_my_user_info(self, find_my_user_info_model: FindMyUserInfoModel):
        user = await self.user_repo.find_user_by_user_id(
            find_my_user_info_model.user_id
        )

        if user is None:
            raise NotFoundUserError

        return FindMyUserInfoResponseModel.model_validate(user)

    def __generate_token(self, user: User):
        access_dict = {"user_id": user.id, "email": user.email}
        refresh_dict = {"user_id": user.id}

        return LoginResponseModel(
            access_token=self.jwt_encoder.encode(
                access_dict,
                self.ACCESS_TOKEN_EXPIRE_MINUTES,
                self.secret_key,
                self.algorithm,
            ),
            refresh_token=self.jwt_encoder.encode(
                refresh_dict,
                self.REFRESH_TOKEN_EXPIRE_MINUTES,
                self.secret_key,
                self.algorithm,
            ),
        )
