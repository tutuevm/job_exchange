from src.UserRating.models import UserRating
from src.utils.repository import SQLAlchemyRepository


class UserRatingRepository(SQLAlchemyRepository):
    model = UserRating
