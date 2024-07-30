from sqlalchemy import select, or_
from sqlalchemy.orm import selectinload
from fastapi import HTTPException, status

from src.utils.repository import SQLAlchemyRepository
from src.models.User import User




class UserRepository(SQLAlchemyRepository):
    model = User

    async def append_many_to_many_elem(self, user_id, elem_model, elem_id, row_name) -> dict:
        user = await self.session.scalar(select(self.model).filter_by(id=user_id).options(selectinload(getattr(User, row_name))))
        elem =  await self.session.scalar(select(elem_model).filter_by(id=elem_id))
        user_relationship = getattr(user, row_name)
        if elem in user_relationship:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='relationship is already exist')
        user_relationship.append(elem)
        return user_relationship

    async def remove_many_to_many_elem(self, user_id, elem_model, elem_id, row_name) -> dict:
        user = await self.session.scalar(
            select(self.model).filter_by(id=user_id).options(selectinload(getattr(User, row_name))))
        elem = await self.session.scalar(select(elem_model).filter_by(id=elem_id))
        user_relationship = getattr(user, row_name)
        if elem not in user_relationship:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='relation does not exist')
        user_relationship.remove(elem)
        return {'status': 'OK'}

    async def get_users_by_different_fields(self, *filter_by):
        query = select(self.model).where(or_(*filter_by))
        result = await self.session.execute(query)
        result = [row[0] for row in result.all()]
        return result

    async def get_all_relationship_elements(self, user_id, row_name) -> dict:
        user = await self.session.scalar(
            select(self.model).filter_by(id=user_id).options(selectinload(getattr(User, row_name))))
        user_relationship = getattr(user, row_name)
        return user_relationship