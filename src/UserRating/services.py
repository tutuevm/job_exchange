from uuid import UUID

from src.UserRating.schemas import UserRatingCreateSchema
from src.utils.UnitOfWork import InterfaceUnitOfWork


class UserRatingService:

    async def add_rating(
        self, uow: InterfaceUnitOfWork, rating: UserRatingCreateSchema, rated_by: UUID
    ):
        rating_data = rating.model_dump()
        rating_data["rated_by"] = rated_by
        async with uow:
            await uow.user_rating.add_one(rating_data)
