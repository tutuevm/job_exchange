from fastapi import APIRouter

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