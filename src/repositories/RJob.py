from src.utils.repository import SQLAlchemyRepository
from src.models.User import Job


class JobRepository(SQLAlchemyRepository):
    model = Job