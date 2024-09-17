from src.ActionType.router import action_type_router
from src.Job.router import job_router
from src.Notification.router import notification_router
from src.Organization.router import organization_router
from src.Place.router import place_router
from src.User.router import user_router
from src.UserAttribute.router import user_attribute_router
from src.auth.auth_router import auth_router

router_list = [
    place_router,
    action_type_router,
    user_attribute_router,
    user_router,
    job_router,
    organization_router,
    auth_router,
    notification_router,
]
