from uuid import UUID

from fastapi import APIRouter

from src.UserAttribute.schemas import AttributeSchema
from src.UserAttribute.services import UserAttributeService
from src.depends import UOWDependence

user_attribute_router = APIRouter(prefix="/user_attr", tags=["attr"])


@user_attribute_router.post("/add_attr")
async def add_attribute(attribute: AttributeSchema, uow: UOWDependence):
    status = await UserAttributeService().add_attr(attribute=attribute, uow=uow)
    return status


@user_attribute_router.post("/get_by_id")
async def get_by_id(attr_id: UUID, uow: UOWDependence):
    elem = await UserAttributeService().get_attr_by_id(uow=uow, filter_id=attr_id)
    return elem


@user_attribute_router.get("/get_all")
async def get_all_attributes(uow: UOWDependence):
    place_title = await UserAttributeService().get_all_attributes(uow=uow)
    return place_title
