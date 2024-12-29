from src.service.user import UserService
from src.service.model import SignUpModel
from src.repository.user import UserRepository
from src.common.entity.user import UserModel
class UserServiceImpl(UserService):
    def __init__(self, user_repository : UserRepository):
        self.user_repo = user_repository
        
    async def create_user(self, sign_up_model: SignUpModel):
        sign_up_model.hashed_password()
        await self.user_repo.insert(
            user_model= UserModel(**sign_up_model.model_dump())
        )
        
        
        