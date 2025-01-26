from fastapi import APIRouter, Depends
from service.model.user.logout_model import LogoutRequest
from src.service.model.find_my_user_info_model import (
    FindMyUserInfoModel,
    FindMyUserInfoResponseModel,
)
from src.service.model.renew_token_model import RenewTokenModel
from src.service.user.jwt_user_auth import (
    JWTUserAuth,
    get_access_token,
    get_token_data,
)
from src.controller.model.renew_token_body_model import RenewTokenBodyModel
from src.controller.model.response import BaseResponse, BaseResponseData
from src.service.model.login_model import LoginResponseModel
from src.controller.model import SignUpBodymodel, LoginBodyModel
from dependency_injector.wiring import inject, Provide
from src.service.model import SignUpModel, LoginModel
from src.service.user import UserService
from container import AppContainer

user_router = APIRouter()


@user_router.post(path="/signup", summary="회원가입 API", response_model=BaseResponse)
@inject
async def sign_up(
    signup_body_model: SignUpBodymodel,
    user_service: UserService = Depends(Provide[AppContainer.user_service]),
):
    await user_service.create_user(SignUpModel(**signup_body_model.model_dump()))

    return BaseResponse()


@user_router.post(
    path="/login",
    summary="로그인 API",
    response_model=BaseResponseData[LoginResponseModel],
)
@inject
async def login(
    login_body_model: LoginBodyModel,
    user_service: UserService = Depends(Provide[AppContainer.user_service]),
):
    response = await user_service.login(LoginModel(**login_body_model.model_dump()))
    return BaseResponseData(result=response)


@user_router.post(
    path="/refresh/renew",
    summary="access 토큰 재발행 API",
    response_model=BaseResponseData[LoginResponseModel],
)
@inject
async def renew_refresh_token(
    renew_token_body_model: RenewTokenBodyModel,
    user_service: UserService = Depends(Provide[AppContainer.user_service]),
):
    result = await user_service.renew_token(
        RenewTokenModel(**renew_token_body_model.model_dump())
    )

    return BaseResponseData(result=result)


@user_router.get(
    path="/get/myinfo",
    summary="내 정보 가져오기 API",
    response_model=BaseResponseData[FindMyUserInfoResponseModel],
    dependencies=[Depends(JWTUserAuth())],
)
@inject
async def get_my_info(
    service: UserService = Depends(Provide[AppContainer.user_service]),
    token_info: dict = Depends(get_token_data),
):
    print(token_info)
    result = await service.get_my_user_info(
        FindMyUserInfoModel(user_id=token_info["user_id"])
    )

    return BaseResponseData(result=result)


@user_router.get(
    path="/logout",
    summary="로그아웃 API",
    response_model=BaseResponse,
    dependencies=[Depends(JWTUserAuth())],
)
@inject
async def logout(
    service: UserService = Depends(Provide[AppContainer.user_service]),
    token_info: dict = Depends(get_token_data),
    access_token: str = Depends(get_access_token),
):
    await service.logout(
        LogoutRequest(access_token=access_token, exp=token_info["exp"])
    )
    return BaseResponse
