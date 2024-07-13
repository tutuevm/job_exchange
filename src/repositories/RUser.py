from src.utils.repository import SQLAlchemyRepository
from src.models.User import User




class UserRepository(SQLAlchemyRepository):
    model = User
