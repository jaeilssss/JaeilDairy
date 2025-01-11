from pydantic import BaseModel


class FindMyUserInfoModel(BaseModel):
    user_id: int


class FindMyUserInfoResponseModel(BaseModel):
    email: str
    name: str
    phone_number: str

    model_config = {"from_attributes": True}
