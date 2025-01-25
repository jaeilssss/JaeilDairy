from pydantic import BaseModel


class DeleteMySchedule(BaseModel):
    schedule_id: int
    user_id: int
