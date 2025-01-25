from pydantic import BaseModel

from src.common.enum.schedule_type_enum import ScheduleTypeEnum


class GetMySchedule(BaseModel):
    user_id: int
    type: ScheduleTypeEnum
    start_date: str
    end_date: str
