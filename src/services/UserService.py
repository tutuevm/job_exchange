from uuid import UUID

from src.models.User import UserAttribute, User
from src.schemas.UserSchema import UserSchema
from src.utils.UnitOfWork import InterfaceUnitOfWork
from src.auth.UserManager import UserManager

class UserService:

    async def register_user(self, uow:InterfaceUnitOfWork, user: UserSchema) -> dict:
        user_data = user.model_dump()
        async with uow:
            user_data['hashed_password'] = UserManager().hash_password(user_data['hashed_password'])
            await uow.user.add_one(user_data)
        return {"status": "OK"}

    async def append_user_attribute(self, uow:InterfaceUnitOfWork, user_id: UUID, attr_id: UUID) -> dict:
        async with uow:
            result = await uow.user.append_many_to_many_elem(user_id=user_id, elem_model=UserAttribute, elem_id=attr_id)
        return {
            "user" : result.full_name,
            "attributes" : result.attributes
        }