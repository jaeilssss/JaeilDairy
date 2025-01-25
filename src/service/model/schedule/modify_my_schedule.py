from pydantic import BaseModel

from src.common.enum.schedule_type_enum import ScheduleTypeEnum


class ModifyMySchedule(BaseModel):
    user_id: int
    schedule_id: int
    title: str
    content: str
    date: str
    type: ScheduleTypeEnum
