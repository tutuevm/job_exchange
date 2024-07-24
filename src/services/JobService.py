from typing import List

from src.schemas.JobSchema import JobSchema
from src.utils.UnitOfWork import InterfaceUnitOfWork
from uuid import UUID
from sqlalchemy.exc import IntegrityError


class JobService:

    async def create_job(self, uow: InterfaceUnitOfWork, job: JobSchema) -> dict:
        job_data = job.model_dump()
        async with uow:
            status = await uow.job.add_one(job_data)
        return status

    async def get_all_jobs(self, uow: InterfaceUnitOfWork) -> List:
        async with uow:
            jobs = await uow.job.get_all()
        return jobs

    async def delete_job_by_id(self, uow: InterfaceUnitOfWork, id: UUID):
        async with uow:
            try:
                status = await uow.job.delete_one(id=id)
                return status
            except IntegrityError:
                return {'status': 'failed',
                        'error': f'There are still references to id={id} in other database tables'}

    async def get_all_responded_users(self, uow: InterfaceUnitOfWork, job_id: UUID):
        async with uow:
            users = await uow.job.get_relationship(job_id, 'responded_users')
        return users



