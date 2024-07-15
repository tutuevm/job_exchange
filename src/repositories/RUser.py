from sqlalchemy import select
from sqlalchemy.orm import selectinload

from src.utils.repository import SQLAlchemyRepository
from src.models.User import User




class UserRepository(SQLAlchemyRepository):
    model = User

    async def append_many_to_many_elem(self, user_id, elem_model, elem_id):
        user = await self.session.scalar(select(self.model).filter_by(id=user_id).options(selectinload(self.model.attributes)))
        elem =  await self.session.scalar(select(elem_model).filter_by(id=elem_id))
        user.attributes.append(elem)
        return user