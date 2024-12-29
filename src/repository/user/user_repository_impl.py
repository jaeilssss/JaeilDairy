from src.repository.user import UserRepository
from sqlalchemy.ext.asyncio import AsyncSession
from src.common.entity.user.user_model import UserModel
class UserRepositoryImpl(UserRepository):
    def __init__(self, session : AsyncSession):
        self.db = session
    
    async def insert(self, user_model: UserModel):
        self.db.add(user_model)
        await self.db.commit()
    
    