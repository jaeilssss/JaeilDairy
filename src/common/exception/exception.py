from typing import Optional
from fastapi import status


class BaseExceptionHanlder(Exception):
    message: str = "error"
    status_code: int = status.HTTP_400_BAD_REQUEST
    code: str = "error"
