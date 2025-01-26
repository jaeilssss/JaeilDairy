from pydantic import BaseModel


class FindAllScheduleRequestModel(BaseModel):
    title: str
    content: str
    date: str
    type: str


class FindAllScheduleResponseModel(BaseModel):

    pass
