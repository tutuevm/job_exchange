from uuid import UUID

from fastapi import APIRouter

from src.ActionType.schemas import ActionTypeSchema
from src.ActionType.services import ActionTypeService
from src.depends import UOWDependence

action_type_router = APIRouter(prefix="/action_type", tags=["job references"])


@action_type_router.get("/get_all")
async def get_place(uow: UOWDependence):
    place_title = await ActionTypeService().get_all_types(uow=uow)
    return place_title


@action_type_router.post("/add_action_type")
async def add_action_type(type_schema: ActionTypeSchema, uow: UOWDependence):
    status = await ActionTypeService().add_type(uow=uow, type_schema=type_schema)
    return status


@action_type_router.post("/get_action_type")
async def get_action_type_by_id(type_id: UUID, uow: UOWDependence):
    place_title = await ActionTypeService().get_type_by_id(uow=uow, type_id=type_id)
    return place_title
