from datetime import datetime
from pydantic import BaseModel

from src.common.enum.schedule_type_enum import ScheduleTypeEnum


class PutModifyMyScheduleBodyModel(BaseModel):
    title: str
    content: str
    date: str
    type: ScheduleTypeEnum
