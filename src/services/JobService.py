from typing import List
from uuid import UUID
from fastapi import HTTPException, status

from src.schemas.JobResponseType import JobResponseType
from src.schemas.JobSchema import JobSchema, JobFilter, JobStatusSchema
from src.utils.UnitOfWork import InterfaceUnitOfWork
from sqlalchemy.exc import IntegrityError


class JobService:

    async def create_job(self, uow: InterfaceUnitOfWork, job: JobSchema) -> dict:
        job_data = job.model_dump()
        async with uow:
            status = await uow.job.add_one(job_data)
        return status

    async def get_jobs(self, uow: InterfaceUnitOfWork, filter: JobFilter) -> List:
        async with uow:
            jobs = await uow.job.get_jobs_by_filter(filter=filter)
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

    async def accept_responded_user(self, uow: InterfaceUnitOfWork, user_id: UUID, job_id: UUID):
        async with uow:
            current_status = await uow.user_job_association.get_association(user_id=user_id, job_id=job_id)
            if current_status.response_status != JobResponseType.SUBMITTED:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Invalid response status. Expected - {JobResponseType.SUBMITTED}, arrived - {current_status.response_status}' )
            result = await uow.user_job_association.change_status_association(user_id=user_id, job_id=job_id, status=JobResponseType.ACCEPTED)
        return result


    async def accept_and_close_job(self, uow: InterfaceUnitOfWork, job_id: UUID):
        async with uow:
            job = await uow.job.find_by_filter(id=job_id)
            if job[0].status_value != JobStatusSchema.COMPLETED.name:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f'Invalid job status. Expected - {JobStatusSchema.COMPLETED.name}'
                )
            result = await uow.job.update_value(elem=job, status_id=JobStatusSchema.CLOSED.name)
            return result
