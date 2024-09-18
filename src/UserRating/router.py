from fastapi import APIRouter, Depends

from src.UserRating.schemas import UserRatingCreateSchema
from src.UserRating.services import UserRatingService
from src.auth.auth_router import check_user
from src.depends import UOWDependence

user_rating = APIRouter(prefix="/user_rating", tags=["user_rating"])


@user_rating.post("/add", status_code=201)
async def add_rating(
    uow: UOWDependence,
    rating: UserRatingCreateSchema,
    rated_by: dict = Depends(check_user),
):
    await UserRatingService().add_rating(
        uow=uow, rating=rating, rated_by=rated_by["id"]
    )
    return
