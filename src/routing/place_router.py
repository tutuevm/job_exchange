from fastapi import APIRouter

from src.depends import UOWDependence
from src.schemas.PlaceSchema import PlaceSchema
from src.services.PlaceService import PlaceService

place_router = APIRouter(
    prefix='/place',
    tags=["Place"]
)

@place_router.post("/add_place")
async def add_place(
        place: PlaceSchema,
        uow: UOWDependence
):
    place_id = await add_place(uow=uow, place=place)
    return {'id': place_id}

@place_router.post('/get_place')
async def get_place(
        place_id : int,
        uow: UOWDependence
):
    place_title = await PlaceService().get_place_by_id(uow=uow, id=place_id)
    return place_title

@place_router.post('/get_all')
async def get_place(
        uow: UOWDependence
):
    place_title = await PlaceService().get_all(uow=uow)
    return place_title