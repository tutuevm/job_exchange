from src.Organization.models import Organization
from src.utils.repository import SQLAlchemyRepository


class OrganizationRepository(SQLAlchemyRepository):
    model = Organization
