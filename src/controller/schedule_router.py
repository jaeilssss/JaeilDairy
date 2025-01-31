from fastapi import APIRouter, Depends, Path
from dependency_injector.wiring import Provide, inject
from container import AppContainer
from src.controller.model.response import BaseResponse, BaseResponseData
from src.service.model.schedule.delete_my_schedule import DeleteMySchedule
from src.service.model.schedule.modify_my_schedule import ModifyMySchedule
from src.controller.model.schedule.put_modify_my_schedule_body_model import (
    PutModifyMyScheduleBodyModel,
)
from src.service.model.schedule.get_my_schedule import GetMySchedule
from src.controller.model.schedule.get_schedule_query_model import GetScheduleQueryModel
from src.service.model.schedule.create_my_schedule import CreateMySchedule
from src.controller.model.schedule import CreateScheduleModel
from src.service.schedule.schedule_service import ScheduleService
from src.service.user.jwt_user_auth import JWTUserAuth, get_token_data


schedule_router = APIRouter()


@schedule_router.post(
    path="/write/post", summary="일정 작성 API", dependencies=[Depends(JWTUserAuth())]
)
@inject
async def create_schedule(
    create_schedule_model: CreateScheduleModel,
    service: ScheduleService = Depends(Provide[AppContainer.schedule_service]),
    token_info: dict = Depends(get_token_data),
):
    await service.create_schedule(
        CreateMySchedule(
            **create_schedule_model.model_dump(), user_id=token_info["user_id"]
        )
    )
    return BaseResponse()


@schedule_router.get(
    path="/my/schedule",
    summary="내 일정 가져오기 API",
    dependencies=[Depends(JWTUserAuth())],
)
@inject
async def get_my_schdule(
    get_schedule_query_model: GetScheduleQueryModel = Depends(
        GetScheduleQueryModel.as_query
    ),
    service: ScheduleService = Depends(Provide[AppContainer.schedule_service]),
    token_info: dict = Depends(get_token_data),
):
    result = await service.get_my_schedule(
        GetMySchedule(
            **get_schedule_query_model.model_dump(), user_id=token_info["user_id"]
        )
    )
    return BaseResponseData(result=result)


@schedule_router.put(
    path="/schedule/{schedule_id}",
    summary="일정 수정하기",
    dependencies=[Depends(JWTUserAuth())],
)
@inject
async def modify_my_schedule(
    put_modify_my_schedule_body_model: PutModifyMyScheduleBodyModel,
    schedule_id: int = Path(..., description="수정 하려고 하는 schedule id"),
    service: ScheduleService = Depends(Provide[AppContainer.schedule_service]),
    token_info: dict = Depends(get_token_data),
):
    await service.modify_my_schedule(
        ModifyMySchedule(
            **put_modify_my_schedule_body_model.model_dump(),
            schedule_id=schedule_id,
            user_id=token_info["user_id"]
        )
    )
    return BaseResponse()


@schedule_router.delete(
    path="/schedule/{schedule_id}",
    summary="스케줄 삭제하기 API",
    dependencies=[Depends(JWTUserAuth())],
)
@inject
async def delete_my_schedule(
    schedule_id: int,
    service: ScheduleService = Depends(Provide[AppContainer.schedule_service]),
    token_info: dict = Depends(get_token_data),
):
    await service.delete_my_schedule(
        DeleteMySchedule(schedule_id=schedule_id, user_id=token_info["user_id"])
    )

    return BaseResponse()
