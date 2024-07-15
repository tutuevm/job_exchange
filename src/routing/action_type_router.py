from fastapi import APIRouter
from uuid import UUID

from src.schemas.ActionTypeScheme import ActionTypeSchema
from src.depends import UOWDependence
from src.services.ActionTypeService import ActionTypeService

action_type_router = APIRouter(
    prefix='/action_type',
    tags=["action_type"]
)


@action_type_router.post("/add_action_type")
async def add_action_type(
        type_schema: ActionTypeSchema,
        uow: UOWDependence
):
    status = await ActionTypeService().add_type(uow=uow, type_schema=type_schema)
    return status

@action_type_router.post('/get_action_type')
async def get_action_type(
        type_id : UUID,
        uow: UOWDependence
):
    place_title = await ActionTypeService().get_type_by_id(uow=uow, type_id=type_id)
    return place_title
