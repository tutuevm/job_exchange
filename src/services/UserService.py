from src.schemas.UserSchema import UserSchema
from src.utils.UnitOfWork import InterfaceUnitOfWork
from src.auth.UserManager import UserManager

class UserService:

    async def register_user(self, uow:InterfaceUnitOfWork, user: UserSchema) -> dict:
        user_data = user.model_dump()
        async with uow:
            user_data['password'] = UserManager().hash_password(user_data['password'])
            await uow.user.add_one(user_data)
        return {"status": "OK"}