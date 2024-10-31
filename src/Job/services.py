from uuid import UUID

from fastapi import HTTPException, status

from src.Job.schemas import (
    JobSchema,
    JobFilter,
    JobStatusSchema,
    JobResponseType,
    AcceptDataSchema,
)
from src.Transaction.schemas import TransactionType, TransactionStatus
from src.utils.UnitOfWork import InterfaceUnitOfWork


class JobService:

    async def create_job(self, uow: InterfaceUnitOfWork, job: JobSchema) -> dict:
        job_data = job.model_dump()
        async with uow:
            status = await uow.job.add_one(job_data)
        return status

    async def get_jobs(self, uow: InterfaceUnitOfWork, filter: JobFilter) -> list:
        async with uow:
            jobs = await uow.job.get_jobs_by_filter(filter=filter)
        result = [{"job": elem} for elem in jobs]
        return result

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

    async def accept_and_close_job(
        self,
        uow: InterfaceUnitOfWork,
        user_id: UUID,
        job_id: UUID,
        current_user,
        accept_data: AcceptDataSchema,
    ):
        async with uow:
            job_response = await uow.user_job_association.get_association(
                user_id=user_id, job_id=job_id
            )
            job = await uow.job.find_by_filter(id=job_id)
            if job[0].owner_id != current_user["id"]:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"only the owner of the work can change this status",
                )
            if job_response.response_status != JobResponseType.ACCEPTED:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Invalid response status. Expected - {JobResponseType.ACCEPTED}, arrived - {job_response.response_status.value}",
                )
            await uow.job.update_value(job[0], status_value=JobStatusSchema.CLOSED)
            amount = (job[0].price * accept_data.hours) * (accept_data.kpi / 100)
            await uow.transaction.add_one(
                {
                    "user_id": user_id,
                    "amount": amount,
                    "type": TransactionType.DEPOSIT,
                    "status": TransactionStatus.COMPLETED,
                }
            )
