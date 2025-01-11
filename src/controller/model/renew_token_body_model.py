from pydantic import BaseModel


class RenewTokenBodyModel(BaseModel):
    refresh_token: str
