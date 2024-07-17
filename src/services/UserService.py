from uuid import UUID

from src.models.User import UserAttribute, Job, User
from src.schemas.UserSchema import UserSchema
from src.utils.UnitOfWork import InterfaceUnitOfWork
from src.utils.UserManager import UserManager

class UserService:

    async def get_all_users(self, uow: InterfaceUnitOfWork):
        '''delete after testing'''
        async with uow:
            place_title = await uow.user.get_all()
            return place_title

    async def register_user(self, uow:InterfaceUnitOfWork, user: UserSchema) -> dict:
        user_data = user.model_dump()
        async with uow:
            user_data['hashed_password'] = UserManager().hash_password(user_data['hashed_password'])
            await uow.user.add_one(user_data)
        return {"status": "OK"}

    async def append_user_attribute(self, uow:InterfaceUnitOfWork, user_id: UUID, attr_id: UUID) -> dict:
        async with uow:
            result = await uow.user.append_many_to_many_elem(user_id=user_id, elem_model=UserAttribute, elem_id=attr_id, row_name="attributes")

        if 'warning' in result:
            return result

        return {
            "user" : result.full_name,
            "attributes" : result.attributes,
            "status" : 'the user is assigned an attribute'
        }

    async def assign_with_job(self, uow: InterfaceUnitOfWork, user_id: UUID, job_id: UUID) -> dict:
        async with uow:
            result = await uow.user.append_many_to_many_elem(user_id=user_id, elem_model=Job, elem_id=job_id, row_name="assigned_jobs")
        if 'warning' in result:
            return result
        return result

    async def unassign_with_job(self, uow: InterfaceUnitOfWork, user_id: UUID, job_id: UUID) -> dict:
        async with uow:
            result = await uow.user.remove_many_to_many_elem(user_id=user_id, elem_model=Job, elem_id=job_id, row_name="assigned_jobs")
            return result