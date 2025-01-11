from pydantic import BaseModel


class RenewTokenModel(BaseModel):
    refresh_token: str
