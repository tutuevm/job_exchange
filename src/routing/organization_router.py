from fastapi import APIRouter

from src.schemas.OrganizationSchema import OrganizationSchema
from src.depends import UOWDependence
from src.services.OrganizationService import OrgganzationService

organization_router = APIRouter(
    prefix = '/organization',
    tags=['job references']
)



@organization_router.post('/create_new')
async def create_new_organization(
        uow: UOWDependence,
        org: OrganizationSchema
):
    result = await OrgganzationService().create_new_organization(uow=uow,org=org)
    return result

@organization_router.get('/get_all')
async def get_all_organizations(
        uow: UOWDependence,
):
    result = await OrgganzationService().get_all_organizations(uow=uow)
    return result