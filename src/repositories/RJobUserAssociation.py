from sqlalchemy import select, update, and_, Row
from uuid import UUID

from src.utils.repository import SQLAlchemyRepository
from src.models.User import user_job_association


class UserJobAssociationRepository(SQLAlchemyRepository):
    model = user_job_association

    async def get_association(self, user_id: UUID, job_id: UUID) -> Row:
        query = select(self.model).where(and_(self.model.c.user_id == user_id, self.model.c.job_id == job_id))
        result = await self.session.execute(query)
        return result.all()[0]

    async def change_status_association(self, user_id: UUID, job_id: UUID, status):
        stmt = update(self.model).where(and_(self.model.c.user_id == user_id, self.model.c.job_id == job_id)).values(
            response_status=status)
        result = await self.session.execute(stmt)
        return result
