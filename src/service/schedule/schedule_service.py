from abc import ABCMeta, abstractmethod

from src.service.model.schedule.delete_my_schedule import DeleteMySchedule
from src.service.model.schedule.modify_my_schedule import ModifyMySchedule
from src.service.model.schedule.get_my_schedule import GetMySchedule
from src.service.model.schedule.create_my_schedule import CreateMySchedule


class ScheduleService(metaclass=ABCMeta):
    @abstractmethod
    async def create_schedule(self, create_my_schedule: CreateMySchedule):
        pass

    @abstractmethod
    async def get_my_schedule(self, get_my_schedule: GetMySchedule):
        pass

    @abstractmethod
    async def modify_my_schedule(self, modify_my_schedule: ModifyMySchedule):
        pass

    @abstractmethod
    async def delete_my_schedule(self, delete_my_schedule: DeleteMySchedule):
        pass
