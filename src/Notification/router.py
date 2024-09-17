from fastapi import APIRouter, Depends

from src.Notification.schemas import NotificationMarkReadSchema
from src.Notification.services import NotificationService
from src.auth.auth_router import check_user
from src.depends import UOWDependence

notification_router = APIRouter(prefix="/notif", tags=["notif"])


@notification_router.get("/user_unread_notif")
async def get_user_unread_notif(
    uow: UOWDependence, current_user: dict = Depends(check_user)
):
    return await NotificationService().get_user_unread_notifications(
        uow=uow, current_user=current_user
    )


@notification_router.patch("/mark_as_read")
async def mark_notif_as_read(
    uow: UOWDependence, notif_list: NotificationMarkReadSchema
):
    return await NotificationService().mark_notifications_as_read(
        uow=uow, notif_list=notif_list
    )
