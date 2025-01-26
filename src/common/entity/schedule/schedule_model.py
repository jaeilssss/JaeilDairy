from pydantic import BaseModel
from sqlalchemy import Column, ForeignKey, Integer, func, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Enum
from src.common.entity.user.user_model import User

# schedule_model.py
from src.common.enum.schedule_type_enum import ScheduleTypeEnum
from database import Base


class Schedule(Base):
    __tablename__ = "schedule"

    id = Column(Integer, primary_key=True, autoincrement=True, name="schedule_id")
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    date = Column(String)
    type = Column(Enum(ScheduleTypeEnum), nullable=False)
    created_at = Column(DateTime, default=func.now())  # 레코드 생성 시 현재 시간
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    user_id = Column(Integer, ForeignKey("user.user_id"))

    user = relationship("User")


class ScheduleResponse(BaseModel):
    title: str
    content: str
    date: str
    type: ScheduleTypeEnum
    user_name: str

    @classmethod
    def convert(cls, schedule: Schedule):
        return cls(
            title=schedule.title,
            content=schedule.content,
            date=schedule.content,
            type=schedule.type,
            user_name=schedule.user.name,
        )
