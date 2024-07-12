from typing import List

from src.schemas.PlaceSchema import PlaceSchema
from src.utils.UnitOfWork import InterfaceUnitOfWork


class PlaceService:

    async def add_place(self, uow: InterfaceUnitOfWork, place: PlaceSchema) -> int:
        place_dict = place.model_dump()
        async with uow:
            place_id = await uow.place.add_one(place_dict)
            return place_id

    async def get_place_by_id(self, uow: InterfaceUnitOfWork, id: int):
        async with uow:
            place_title = await uow.place.find_by_filter(id=id)
            return place_title

    async def get_all(self, uow: InterfaceUnitOfWork):
        async with uow:
            place_title = await uow.place.get_all()
            return place_title
