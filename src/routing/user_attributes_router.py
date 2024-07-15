from fastapi import APIRouter
from uuid import UUID

from src.schemas.AttributeSchema import AttributeSchema
from src.services.UserAttributeService import UserAttributeService
from src.depends import UOWDependence

user_attribute_router = APIRouter(
    prefix='/user_attr',
    tags=['attr']
)


@user_attribute_router.post('/add_attr')
async def add_attribute(
        attribute: AttributeSchema,
        uow: UOWDependence
):
    status = await UserAttributeService().add_attr(attribute=attribute, uow=uow)
    return status

@user_attribute_router.post('/get_by_id')
async def get_by_id(
        attr_id : UUID,
        uow: UOWDependence
):
    elem = await UserAttributeService().get_attr_by_id(uow=uow, filter_id=attr_id)
    print(type(elem))
    return elem