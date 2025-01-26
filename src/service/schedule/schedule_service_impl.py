import json
from service.model.schedule.get_my_schedule import GetMySchedule
from service.redis.redis_service import RedisService
from src.common.exception.schedule_exception import NotDeleteException
from src.service.model.schedule.delete_my_schedule import DeleteMySchedule
from src.service.model.schedule.modify_my_schedule import ModifyMySchedule
from src.repository.model.schedule.update_schedule_request_model import (
    UpdateScheduleRequestModel,
)
from src.repository.model.schedule.find_all_schedule_request_model import (
    FindAllScheduleRequestModel,
)
from src.repository.schedule.schedule_repository import ScheduleRepository
from src.service.model.schedule.create_my_schedule import CreateMySchedule
from src.service.schedule.schedule_service import ScheduleService
from src.common.entity.schedule.schedule_model import Schedule, ScheduleResponse


class ScheduleServiceImpl(ScheduleService):
    def __init__(
        self, schedule_repository: ScheduleRepository, redis_service: RedisService
    ):
        self.schedule_repo = schedule_repository
        self.redis_service = redis_service

    async def create_schedule(self, create_my_schedule: CreateMySchedule):
        schedule = Schedule(**create_my_schedule.model_dump())
        await self.schedule_repo.create_schedule(schedule)

    async def get_my_schedule(self, get_my_schedule: GetMySchedule):

        response = await self.schedule_repo.find_all_my_schedule(
            FindAllScheduleRequestModel(**get_my_schedule.model_dump())
        )

        return [ScheduleResponse.convert(schedule) for schedule in response]

    async def modify_my_schedule(self, modify_my_schedule: ModifyMySchedule):
        await self.schedule_repo.update_schedule(
            UpdateScheduleRequestModel(**modify_my_schedule.model_dump())
        )

    async def delete_my_schedule(self, delete_my_schedule: DeleteMySchedule):
        result = await self.schedule_repo.delete_schedule_by_schedule_id_and_user_id(
            schedule_id=delete_my_schedule.schedule_id,
            user_id=delete_my_schedule.user_id,
        )

        if not result:
            raise NotDeleteException
