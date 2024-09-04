from fastapi import APIRouter

from src.Organization.schemas import OrganizationSchema
from src.Organization.services import OrganizationService
from src.depends import UOWDependence

organization_router = APIRouter(prefix="/organization", tags=["job references"])


@organization_router.post("/create_new")
async def create_new_organization(uow: UOWDependence, org: OrganizationSchema):
    result = await OrganizationService().create_new_organization(uow=uow, org=org)
    return result


@organization_router.get("/get_all")
async def get_all_organizations(
    uow: UOWDependence,
):
    result = await OrganizationService().get_all_organizations(uow=uow)
    return result
