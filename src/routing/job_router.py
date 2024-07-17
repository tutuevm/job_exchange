from fastapi import APIRouter
from uuid import UUID


from src.depends import UOWDependence
from src.schemas.JobSchema import JobSchema
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


@job_router.get('/all')
async def get_jobs(uow : UOWDependence):
    result = await JobService().get_all_jobs(uow=uow)
    return result


@job_router.delete('/remove_job')
async def remove_job_by_id(
        uow: UOWDependence,
        job_id : UUID
) -> dict:
    result = await JobService().delete_job_by_id(uow=uow,id=job_id)
    return result