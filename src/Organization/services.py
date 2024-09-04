from src.Organization.schemas import OrganizationSchema
from src.utils.UnitOfWork import InterfaceUnitOfWork


class OrganizationService:

    async def create_new_organization(
        self, uow: InterfaceUnitOfWork, org: OrganizationSchema
    ):
        org_dict = org.model_dump()
        async with uow:
            result = await uow.org.add_one(org_dict)
        return result

    async def get_all_organizations(self, uow: InterfaceUnitOfWork):
        async with uow:
            result = await uow.org.get_all()
        return result
