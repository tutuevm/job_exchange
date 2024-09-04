from fastapi import APIRouter

from src.Place.schemas import PlaceSchema, PlaceByIdSchema
from src.Place.services import PlaceService
from src.depends import UOWDependence

place_router = APIRouter(prefix="/place", tags=["job references"])


@place_router.post("/add_place")
async def add_place(place: PlaceSchema, uow: UOWDependence):
    status = await PlaceService().add_place(uow=uow, place=place)
    return status


@place_router.post("/get_place_by_id")
async def get_place_by_id(place_id: PlaceByIdSchema, uow: UOWDependence):
    place_title = await PlaceService().get_place_by_id(uow=uow, id=place_id.id)
    return place_title


@place_router.get("/get_all")
async def get_all_places(uow: UOWDependence):
    place_title = await PlaceService().get_all(uow=uow)
    return place_title
