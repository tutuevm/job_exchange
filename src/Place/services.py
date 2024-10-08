from uuid import UUID

from src.Place.schemas import PlaceSchema
from src.utils.UnitOfWork import InterfaceUnitOfWork


class PlaceService:

    async def add_place(self, uow: InterfaceUnitOfWork, place: PlaceSchema) -> dict:
        place_dict = place.model_dump()
        async with uow:
            status = await uow.place.add_one(place_dict)
            return status

    async def get_place_by_id(self, uow: InterfaceUnitOfWork, id: UUID):
        async with uow:
            place_title = await uow.place.find_by_filter(id=id)
            return place_title

    async def get_all(self, uow: InterfaceUnitOfWork):
        async with uow:
            place_title = await uow.place.get_all()
            return place_title
