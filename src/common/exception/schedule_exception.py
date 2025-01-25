from src.common.exception.exception import BaseExceptionHanlder
from fastapi import status


class NotDeleteException(BaseExceptionHanlder):
    status_code: int = status.HTTP_400_BAD_REQUEST
    code: str = "SCHEDULE_ERROR_001"
    message: str = "스케줄을 삭제 하는데 실패 했습니다."
