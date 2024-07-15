from uuid import UUID

from src.schemas.JobSchema import JobSchema
from src.utils.UnitOfWork import InterfaceUnitOfWork

class JobService:

    async def create_job(self, uow: InterfaceUnitOfWork, job: JobSchema) -> dict:
        job_data = job.model_dump()
        async with uow:
            status = await uow.job.add_one(job_data)
        return status