from fastapi import Depends, Request

from src.common.exception.user_exception import LogoutJWTError
from container import AppContainer
from src.service.redis import redis_service
from src.service.redis.redis_service import RedisService
from dependency_injector.wiring import Provide, inject

exclusive_end_point = {"/login", "/logout", "/signup", "/refresh/renew"}


@inject
async def blacklist_middleware(
    request: Request,
    call_next,
):
    redis_service = AppContainer.redis_service()
    token = request.headers.get("Authorization")

    if token is not None:
        token = token.replace("Bearer ", "")
        result = await redis_service.get(token)
        if result:
            raise LogoutJWTError

    response = await call_next(request)
    return response
