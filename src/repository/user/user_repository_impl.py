from src.repository.user import UserRepository
from sqlalchemy.ext.asyncio import AsyncSession
from src.common.entity.user.user_model import User
from src.repository.model import FindUserByEmailRequestModel

from sqlalchemy import select


class UserRepositoryImpl(UserRepository):
    def __init__(self, session: AsyncSession):
        self.db = session

    async def insert(self, user_model: User):
        self.db.add(user_model)
        await self.db.commit()

    async def find_user_by_email(
        self, find_user_by_email_model: FindUserByEmailRequestModel
    ):
        result = await self.db.execute(
            select(User).where(User.email == find_user_by_email_model.email)
        )
        return result.scalar_one_or_none()

    async def find_user_by_user_id(self, user_id):
        result = await self.db.execute(select(User).where(User.id == user_id))
        return result.scalar_one_or_none()
