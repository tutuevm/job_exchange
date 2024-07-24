from fastapi import APIRouter, Depends
from uuid import UUID
from typing import Annotated
from pydantic import BaseModel


from src.depends import UOWDependence
from src.schemas.JobSchema import JobSchema, JobFilter
from src.services.JobService import JobService

job_router = APIRouter(
    prefix='/jobs',
    tags=['jobs']
)


@job_router.post('/create')
async def create_job_elem(
        uow : UOWDependence,
        job : JobSchema
) -> dict:
    status = await JobService().create_job(uow=uow, job=job)
    return status


@job_router.get('/get_jobs')
async def get_jobs(
        uow : UOWDependence,
        q: JobFilter = Depends()
):
    result = await JobService().get_all_jobs(uow=uow)
    return result


@job_router.delete('/remove_job')
async def remove_job_by_id(
        uow: UOWDependence,
        job_id : UUID
) -> dict:
    result = await JobService().delete_job_by_id(uow=uow,id=job_id)
    return result

@job_router.post('/get_job_relationship')
async def get_job_relationship(
        uow: UOWDependence,
        job_id : UUID
):
    result = await JobService().get_all_responded_users(uow=uow, job_id=job_id)
    return result