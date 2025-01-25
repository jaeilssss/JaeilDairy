from abc import ABCMeta, abstractmethod

from src.repository.model.schedule.update_schedule_request_model import (
    UpdateScheduleRequestModel,
)
from src.repository.model.schedule.find_all_schedule_request_model import (
    FindAllScheduleRequestModel,
)
from src.common.entity.schedule.schedule_model import Schedule


class ScheduleRepository(metaclass=ABCMeta):

    @abstractmethod
    async def create_schedule(self, schedule: Schedule):
        pass

    @abstractmethod
    async def find_all_my_schedule(
        self, find_my_all_schedule: FindAllScheduleRequestModel
    ):
        pass

    @abstractmethod
    async def update_schedule(self, update_schedule: UpdateScheduleRequestModel):
        pass

    @abstractmethod
    async def delete_schedule_by_schedule_id_and_user_id(
        self, schedule_id: int, user_id: int
    ):
        pass
