from src.repository.user import UserRepository
from sqlalchemy.ext.asyncio import AsyncSession
from src.common.entity.user.user_model import UserModel
from src.repository.model import FindUserByEmailRequestModel

from sqlalchemy import select


class UserRepositoryImpl(UserRepository):
    def __init__(self, session: AsyncSession):
        self.db = session

    async def insert(self, user_model: UserModel):
        self.db.add(user_model)
        await self.db.commit()

    async def find_user_by_email(
        self, find_user_by_email_model: FindUserByEmailRequestModel
    ):
        result = await self.db.execute(
            select(UserModel).where(UserModel.email == find_user_by_email_model.email)
        )
        return result.scalar_one_or_none()

    async def find_user_by_user_id(self, user_id):
        result = await self.db.execute(select(UserModel).where(UserModel.id == user_id))
        print(result)
        print(type(result))
        return result.scalar_one_or_none()
