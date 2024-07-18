from src.utils.repository import SQLAlchemyRepository
from src.models.Organization import Organization


class OrganizationRepository(SQLAlchemyRepository):
    model = Organization