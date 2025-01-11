from typing import Generic, TypeVar
from pydantic import BaseModel


class BaseResponse(BaseModel):
    code: str = "OK"
    data: str = "OK"


T = TypeVar("T")


class BaseResponseData(Generic[T], BaseModel):
    code: str = "OK"
    result: T
