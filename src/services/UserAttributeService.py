from src.schemas.AttributeSchema import AttributeSchema
from src.utils.UnitOfWork import InterfaceUnitOfWork



class UserAttributeService:

    async def add_attr(self, uow: InterfaceUnitOfWork, attribute: AttributeSchema) -> int:
        data = attribute.model_dump()
        async with uow:
            attr_id = await uow.user_attr.add_one(data)
            return attr_id