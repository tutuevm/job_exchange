from fastapi import APIRouter

from src.schemas.place import PlaceSchema

place_router = APIRouter(
    prefix='/place',
    tags=["Place"]
)

@place_router.post("/add_place")
async def add_place(
        place: PlaceSchema,
        uow: UOWDependence
)