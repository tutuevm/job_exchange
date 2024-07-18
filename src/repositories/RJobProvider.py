from src.utils.repository import SQLAlchemyRepository
from src.models.JobProvider import JobProvider


class JobProviderRepository(SQLAlchemyRepository):
    model = JobProvider