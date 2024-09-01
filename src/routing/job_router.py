from typing import Annotated, List
from uuid import UUID

from fastapi import APIRouter, Depends

from src.auth.auth_router import check_user
from src.depends import UOWDependence
from src.schemas.JobSchema import JobSchema, return_filter, JobResponseSchema
from src.services.JobService import JobService

job_router = APIRouter(prefix="/jobs", tags=["jobs"])


@job_router.post("/create")
async def create_job_elem(uow: UOWDependence, job: JobSchema) -> dict:
    status = await JobService().create_job(uow=uow, job=job)
    return status


@job_router.get("/get_jobs", response_model=List[JobResponseSchema])
async def get_jobs(uow: UOWDependence, q: Annotated[dict, Depends(return_filter)]):
    result = await JobService().get_jobs(uow=uow, filter=q)

    return result


@job_router.delete("/remove_job")
async def remove_job_by_id(uow: UOWDependence, job_id: UUID) -> dict:
    result = await JobService().delete_job_by_id(uow=uow, id=job_id)
    return result


@job_router.post("/get_job_relationship")
async def get_job_relationship(uow: UOWDependence, job_id: UUID):
    result = await JobService().get_all_responded_users(uow=uow, job_id=job_id)
    return result


@job_router.put("/accept_responded_user")
async def accept_responded_user(
    uow: UOWDependence, user_id: UUID, job_id: UUID, current_user=Depends(check_user)
):
    result = await JobService().accept_responded_user(
        uow=uow, user_id=user_id, job_id=job_id, current_user=current_user
    )
    return result


@job_router.put("/set_compete_status_job")
async def set_compete_status_job(
    uow: UOWDependence, user_id: UUID, job_id: UUID, current_user=Depends(check_user)
):
    result = await JobService().set_compete_status_job(
        uow=uow, user_id=user_id, job_id=job_id, current_user=current_user
    )
    return result


@job_router.put("/accept_and_close_job")
async def accept_and_close_job(
    uow: UOWDependence, job_id: UUID, current_user=Depends(check_user)
):
    result = await JobService().accept_and_close_job(
        uow=uow, job_id=job_id, current_user=current_user
    )
    return result
