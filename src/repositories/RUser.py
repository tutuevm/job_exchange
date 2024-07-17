from sqlalchemy import select
from sqlalchemy.orm import selectinload

from src.utils.repository import SQLAlchemyRepository
from src.models.User import User




class UserRepository(SQLAlchemyRepository):
    model = User

    async def append_many_to_many_elem(self, user_id, elem_model, elem_id, row_name) -> dict:
        user = await self.session.scalar(select(self.model).filter_by(id=user_id).options(selectinload(getattr(User, row_name))))
        elem =  await self.session.scalar(select(elem_model).filter_by(id=elem_id))
        user_relationship = getattr(user, row_name)
        if elem in user_relationship:
            return {'warning' : 'relations is already exist'}
        user_relationship.append(elem)
        return {
            "user" : user.full_name,
            "job" : user.assigned_jobs,
            "status" : 'the user is assigned a job'
        }

    async def remove_many_to_many_elem(self, user_id, elem_model, elem_id, row_name) -> dict:
        user = await self.session.scalar(
            select(self.model).filter_by(id=user_id).options(selectinload(getattr(User, row_name))))
        elem = await self.session.scalar(select(elem_model).filter_by(id=elem_id))
        if elem not in user.attributes:
            return {
                'warning' : 'relation does not exist'
            }
        user.attributes.remove(elem)
        return {'status': 'OK'}