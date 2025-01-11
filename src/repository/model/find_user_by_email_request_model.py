from pydantic import BaseModel
class FindUserByEmailRequestModel(BaseModel):
    email: str