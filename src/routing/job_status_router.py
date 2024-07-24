from fastapi import APIRouter
from uuid import UUID

from src.depends import UOWDependence
from src.services.JobStatusService import JobStatusService


job_status_router = APIRouter(
    prefix='/job_status',
    tags = ['job references']
)


@job_status_router.get('/get_all')
async def get_all_statuses(
        uow: UOWDependence
):
    result = await JobStatusService().get_all_statuses(uow=uow)
    return result

@job_status_router.post('/create_new')
async def create_new_job_status(
        uow: UOWDependence,
        title: str
):
    result = await JobStatusService().create_job_status(uow=uow, title=title)
    return result

@job_status_router.post('/get_by_id')
async def get_status_by_id(
        uow: UOWDependence,
        id: UUID
):
    result = await JobStatusService().get_status_by_id(uow=uow, status_id=id)
    return result