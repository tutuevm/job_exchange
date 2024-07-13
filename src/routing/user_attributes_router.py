from fastapi import APIRouter

from src.schemas.AttributeSchema import AttributeSchema
from src.services.UserAttributeService import UserAttributeService
from src.depends import UOWDependence


user_attribute_router = APIRouter(
    prefix= '/user_attr',
    tags = ['attr']
)



@user_attribute_router.post('/add_attr')
async def add_attribute(
        attribute: AttributeSchema,
        uow : UOWDependence
):
    attr_id = await UserAttributeService().add_attr(attribute=attribute, uow=uow)
    return {'id':attr_id}