from fastapi.security import HTTPBearer
from fastapi import Request

from src.common.exception.user_exception import (
    JWTBadRequestError,
    JWTExpiredTokenError,
    UserNotUnAuthorizationError,
)
from src.common.function.jwt.jwt_decoder import JWTDecoder


class JWTUserAuth(HTTPBearer):

    def __init__(
        self, *, bearerFormat=None, scheme_name=None, description=None, auto_error=True
    ):
        super(JWTUserAuth, self).__init__(
            bearerFormat=bearerFormat,
            scheme_name=scheme_name,
            description=description,
            auto_error=auto_error,
        )
        self.decoder = JWTDecoder()

    async def __call__(self, request: Request):
        auth_header = request.headers.get("Authorization")

        if auth_header is None:
            raise UserNotUnAuthorizationError

        try:
            token_type, token = auth_header.split(" ")
        except ValueError:
            raise JWTBadRequestError

        if token_type != "Bearer":
            raise JWTBadRequestError
        try:
            payload = self.decoder.decode(token)

            if not payload:
                raise JWTExpiredTokenError

            user_id = payload.get("user_id")
            email = payload.get("email")

            request.state.token_info = payload
            if user_id is None or email is None:
                raise JWTBadRequestError
        except Exception as e:
            raise e
        return await super(JWTUserAuth, self).__call__(request)


def get_token_data(request: Request) -> dict:
    return request.state.token_info
