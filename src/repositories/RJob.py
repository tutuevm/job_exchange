from sqlalchemy import select
from sqlalchemy.orm import selectinload
from uuid import UUID

from src.utils.repository import SQLAlchemyRepository
from src.models.User import Job
from src.models.JobStatus import  JobStatus
from src.models.JobType import JobType


class JobStatusRepository(SQLAlchemyRepository):
    model = JobStatus


class JobTypeRepository(SQLAlchemyRepository):
    model = JobType


class JobRepository(SQLAlchemyRepository):
    model = Job

    async def get_relationship(self, job_id: UUID, row_name: str):
        job = await self.session.scalar(
            select(self.model).filter_by(id=job_id).options(selectinload(getattr(Job, row_name))))
        return getattr(job, row_name)
