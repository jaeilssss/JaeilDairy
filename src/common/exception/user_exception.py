from fastapi import status
from src.common.exception.exception import BaseExceptionHanlder


class ValidationEmailError(BaseExceptionHanlder):
    status_code: int = status.HTTP_409_CONFLICT
    code: str = "USER_ERROR_001"
    message: str = "이미 가입 된 이메일 입니다."


class UserNotFoundError(BaseExceptionHanlder):
    status_code: int = status.HTTP_404_NOT_FOUND
    code: str = "USER_ERROR_002"
    message: str = "해당 유저 정보가 없습니다."


class UserNotUnAuthorizationError(BaseExceptionHanlder):
    status_code: int = status.HTTP_401_UNAUTHORIZED
    code: str = "USER_ERROR_003"
    message: str = "권한이 없는 요청입니다."


class JWTExpiredTokenError(BaseExceptionHanlder):
    status_code: int = status.HTTP_401_UNAUTHORIZED
    code: str = "USER_ERROR_004"
    message: str = "토큰이 만료된 요청 입니다."


class JWTBadRequestError(BaseExceptionHanlder):
    status_code: int = status.HTTP_401_UNAUTHORIZED
    code: str = "USER_ERROR_005"
    message: str = "잘못된 토큰 입니다."


class NotFoundUserError(BaseExceptionHanlder):
    status_code: int = status.HTTP_404_NOT_FOUND
    code: str = "USER_ERROR_006"
    message: str = "유저 정보가 없습니다."
