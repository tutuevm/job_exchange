from fastapi import APIRouter

from src.depends import UOWDependence
from src.schemas.OrganizationSchema import OrganizationSchema
from src.services.OrganizationService import OrganizationService

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
