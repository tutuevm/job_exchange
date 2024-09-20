from uuid import UUID

from sqlalchemy import update

from src.UserData.models import UserData
from src.utils.repository import SQLAlchemyRepository


class UserDataRepository(SQLAlchemyRepository):
    model = UserData

    async def update_data(self, user_id: UUID, update_data: dict):
        stmt = (
            update(self.model)
            .where(self.model.user_id == user_id)
            .values(**update_data)
        )
        await self.session.execute(stmt)
        return
