from typing import List
from uuid import UUID

from fastapi import HTTPException, status

from src.schemas.JobResponseType import JobResponseType
from src.schemas.JobSchema import JobSchema, JobFilter, JobStatusSchema
from src.schemas.TransactionSchema import TransactionType, TransactionStatus
from src.utils.UnitOfWork import InterfaceUnitOfWork


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
            status = await uow.job.delete_one(id=id)
        return status

    async def get_all_responded_users(self, uow: InterfaceUnitOfWork, job_id: UUID):
        async with uow:
            users = await uow.job.get_relationship(job_id, "responded_users")
        return users

    async def accept_responded_user(
        self, uow: InterfaceUnitOfWork, user_id: UUID, job_id: UUID, current_user
    ):
        async with uow:
            job = await uow.job.find_by_filter(id=job_id)
            if job[0].owner_id != current_user["id"]:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"only the owner of the work can change its status",
                )
            job_response = await uow.user_job_association.get_association(
                user_id=user_id, job_id=job_id
            )
            if job_response.response_status != JobResponseType.SUBMITTED:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Invalid response status. Expected - {JobResponseType.SUBMITTED}, arrived - {job_response.response_status}",
                )
            result = await uow.user_job_association.change_status_association(
                user_id=user_id, job_id=job_id, status=JobResponseType.ACCEPTED
            )
        return result

    async def set_compete_status_job(
        self, uow: InterfaceUnitOfWork, user_id: UUID, job_id: UUID, current_user
    ):
        async with uow:
            job_response = await uow.user_job_association.get_association(
                user_id=user_id, job_id=job_id
            )
            job = await uow.job.find_by_filter(id=job_id)
            await uow.transaction.add_one(
                {
                    "user_id": user_id,
                    "amount": job[0].price,
                    "type": TransactionType.DEPOSIT,
                    "status": TransactionStatus.COMPLETED,
                }
            )
            if job[0].owner_id != current_user["id"]:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"only the owner of the work can change its status",
                )
            if job[0].status_value != JobStatusSchema.CRATED:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Invalid response status. Expected - {JobStatusSchema.CRATED.name}, arrived - {job[0].status_value}",
                )
            if job_response.response_status != JobResponseType.ACCEPTED:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Invalid response status. Expected - {JobResponseType.ACCEPTED}, arrived - {job_response.response_status.value}",
                )
            await uow.job.update_value(job[0], status_value=JobStatusSchema.COMPLETED)

    async def accept_and_close_job(
        self, uow: InterfaceUnitOfWork, job_id: UUID, current_user
    ):
        async with uow:
            job = await uow.job.find_by_filter(id=job_id)
            if job[0].status_value != JobStatusSchema.COMPLETED.name:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Invalid job status. Expected - {JobStatusSchema.COMPLETED.name}",
                )
            result = await uow.job.update_value(
                elem=job, status_id=JobStatusSchema.CLOSED.name
            )
            if job[0].owner_id != current_user["id"]:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"only the owner of the work can change its status",
                )
        return result
