from src.auth.auth_router import auth_router
from src.routing.action_type_router import action_type_router
from src.routing.job_router import job_router
from src.routing.organization_router import organization_router
from src.routing.place_router import place_router
from src.routing.user_attributes_router import user_attribute_router
from src.routing.user_router import user_router

router_list = [
    place_router,
    action_type_router,
    user_attribute_router,
    user_router,
    job_router,
    organization_router,
    auth_router,
]
