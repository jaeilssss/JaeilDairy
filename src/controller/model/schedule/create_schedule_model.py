from typing import Optional
from pydantic import BaseModel

from src.common.enum.schedule_type_enum import ScheduleTypeEnum


class CreateScheduleModel(BaseModel):
    title: str
    content: str
    type: ScheduleTypeEnum
    date: Optional[str] = None
