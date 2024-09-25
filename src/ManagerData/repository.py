from uuid import UUID

from src.ManagerData.models import ManagerData
from src.utils.repository import SQLAlchemyRepository


class ManagerDataRepository(SQLAlchemyRepository):
    model = ManagerData

    async def update_data(self, user_id: UUID, update_data: dict):
        stmt = (
            update(self.model)
            .where(self.model.user_id == user_id)
            .values(**update_data)
        )
        await self.session.execute(stmt)
        return