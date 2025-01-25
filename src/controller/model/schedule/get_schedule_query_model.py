from fastapi import Query
from pydantic import BaseModel

from src.common.enum.schedule_type_enum import ScheduleTypeEnum


class GetScheduleQueryModel(BaseModel):
    type: ScheduleTypeEnum
    start_date: str
    end_date: str

    @classmethod
    def as_query(
        cls,
        type: ScheduleTypeEnum = Query(ScheduleTypeEnum.ALL, description="스케줄 타입"),
        start_date: str = Query(..., description="필터 시작 날짜"),
        end_date: str = Query(..., description="필터 종료 날짜"),
    ):
        return cls(type=type, start_date=start_date, end_date=end_date)
