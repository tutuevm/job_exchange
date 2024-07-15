from sqlalchemy import select
from sqlalchemy.orm import selectinload

from src.utils.repository import SQLAlchemyRepository
from src.models.User import User




class UserRepository(SQLAlchemyRepository):
    model = User

    async def append_many_to_many_elem(self, user_id, elem_model, elem_id, row_name) -> User:
        user = await self.session.scalar(select(self.model).filter_by(id=user_id).options(selectinload(getattr(User, row_name))))
        elem =  await self.session.scalar(select(elem_model).filter_by(id=elem_id))
        user_relationship = getattr(user, row_name)
        user_relationship.append(elem)
        return user

    # async def remove_many_to_many_elem(self, user_id, elem_model, elem_id) -> User:
    #     user = await self.session.scalar(
    #         select(self.model).filter_by(id=user_id).options(selectinload(self.model.attributes)))
    #     elem = await self.session.scalar(select(elem_model).filter_by(id=elem_id))
    #     if elem in user.attributes:
    #         user.attributes.remove(elem)
    #
    #     return user