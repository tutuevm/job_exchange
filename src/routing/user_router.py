from fastapi import APIRouter
from uuid import UUID

from src.schemas.UserSchema import UserSchema
from src.depends import UOWDependence
from src.services.UserService import UserService


user_router = APIRouter(
    prefix='/user_manager',
    tags = ['user manager']
)

@user_router.post('/register_user')
async def reg_user(uow:UOWDependence, user: UserSchema) -> dict:
    status = await UserService().register_user(uow=uow, user=user)
    return status

@user_router.post('/append_attr')
async def append_user_attr(uow:UOWDependence,user_id: UUID, attr_id: UUID):
    user = await UserService().append_user_attribute(uow=uow, user_id=user_id,attr_id=attr_id)
    return user

@user_router.post('/assign_with_job')
async def assign_with_job(uow:UOWDependence,user_id: UUID, job_id: UUID):
    result = await UserService().assign_with_job(uow=uow, user_id=user_id,job_id=job_id)
    return result