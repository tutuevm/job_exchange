from src.schemas.AttributeSchema import AttributeSchema
from src.utils.UnitOfWork import InterfaceUnitOfWork
class UserAttributeService:

    async def add_attr(self, uow: InterfaceUnitOfWork, attribute: AttributeSchema):
        data = attribute.model_dump()
        async with uow:
            pass