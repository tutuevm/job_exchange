from fastapi import APIRouter, Depends

from src.auth.auth_router import check_user
from src.depends import UOWDependence

notification_router = APIRouter(prefix="/notif", tags=["Notif"])


@notification_router.get("/user_unread_notif")
async def get_user_unread_notif(
    uow: UOWDependence, current_user: dict = Depends(check_user)
): ...
