from fastapi import APIRouter
from uuid import UUID

from src.depends import UOWDependence
from src.services.JobTypeService import JobTypeService


job_type_router = APIRouter(
    prefix='/job_type',
    tags = ['job references']
)


@job_type_router.get('/get_all')
async def get_all_types(
        uow: UOWDependence
):
    result = await JobTypeService().get_all_types(uow=uow)
    return result

@job_type_router.post('/create_new')
async def create_new_job_type(
        uow: UOWDependence,
        title: str
):
    result = await JobTypeService().create_job_type(uow=uow, title=title)
    return result

@job_type_router.post('/get_by_id')
async def get_type_by_id(
        uow: UOWDependence,
        id: UUID
):
    result = await JobTypeService().get_type_by_id(uow=uow, type_id=id)
    return result