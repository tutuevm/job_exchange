from uuid import UUID

from src.schemas.AttributeSchema import AttributeSchema
from src.utils.UnitOfWork import InterfaceUnitOfWork


class UserAttributeService:

    async def add_attr(
        self, uow: InterfaceUnitOfWork, attribute: AttributeSchema
    ) -> dict:
        data = attribute.model_dump()
        async with uow:
            status = await uow.user_attr.add_one(data)
            return status

    async def get_attr_by_id(self, uow: InterfaceUnitOfWork, filter_id: UUID) -> dict:
        async with uow:
            attr_title = await uow.user_attr.find_by_filter(id=filter_id)
        return attr_title[0]

    async def get_all_attributes(self, uow: InterfaceUnitOfWork):
        async with uow:
            result = await uow.user_attr.get_all()
            return result
