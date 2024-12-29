from fastapi import APIRouter, Depends
from src.controller.model import SignUpBodymodel
from dependency_injector.wiring import inject, Provide
from src.service.model.sign_up_model import SignUpModel
from src.service.user import UserService
from container import AppContainer
user_router = APIRouter()

@user_router.post(
    path= "/signup",
    summary="회원가입 API"
)
@inject
async def sign_up(
    signup_body_model: SignUpBodymodel, 
    user_service: UserService = Depends(Provide[AppContainer.user_service])
):
    await user_service.create_user(
        SignUpModel(**signup_body_model.model_dump())
    )
