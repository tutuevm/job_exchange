from uuid import UUID

from fastapi import APIRouter, HTTPException, Depends
from starlette.responses import JSONResponse

from src.User.schemas import UserSchema, UserAcceptAttrSchema
from src.User.services import UserService
from src.UserData.schemas import UserDataUpdateSchema
from src.auth.auth_router import check_user
from src.depends import UOWDependence

user_router = APIRouter(prefix="/user_manager", tags=["user manager"])


@user_router.get("/get_all")
async def get_all_users(uow: UOWDependence):
    place_title = await UserService().get_all_users(uow=uow)
    return place_title


@user_router.get("/get_user_by_id")
async def get_user_by_id(uow: UOWDependence, user_id: UUID):
    result = await UserService().get_user_by_id(uow=uow, user_id=user_id)
    return result


@user_router.get("/get_balance")
async def get_user_balance(
    uow: UOWDependence, current_user: dict = Depends(check_user)
) -> int:
    result = await UserService().get_user_balance(uow=uow, user=current_user)
    return result


@user_router.get("/get_user_assigned_jobs")
async def get_user_assigned_jobs(
    uow: UOWDependence, current_user: dict = Depends(check_user)
):
    result = await UserService().get_user_assigned_jobs(uow=uow, user=current_user)
    return result


@user_router.get("/get_created_jobs")
async def get_created_jobs(
    uow: UOWDependence, current_user: dict = Depends(check_user)
):
    result = await UserService().get_user_created_job(uow=uow, user=current_user)
    return result


@user_router.put("/update_data")
async def update_user_data(uow: UOWDependence, update_data: UserDataUpdateSchema):
    result = await UserService().update_user_data(
        uow=uow, user_id=update_data.user_id, update_data=update_data.update_data
    )
    return result


@user_router.post("/register_user")
async def reg_user(uow: UOWDependence, user: UserSchema):
    try:
        status = await UserService().register_user(uow=uow, user=user)
        return status
    except HTTPException as e:
        return JSONResponse(status_code=e.status_code, content=e.detail)


@user_router.post("/append_attr")
async def append_user_attr(uow: UOWDependence, data: UserAcceptAttrSchema):
    user = await UserService().append_user_attribute(
        uow=uow, user_id=data.user_id, key=data.key, value=data.value
    )
    return user


@user_router.post("/response_for_job")
async def response_for_job(uow: UOWDependence, user_id: UUID, job_id: UUID):
    result = await UserService().response_for_job(
        uow=uow, user_id=user_id, job_id=job_id
    )
    return result


@user_router.delete("/remove_attribute")
async def unassign_with_job(uow: UOWDependence, user_id: UUID, attr_id: UUID):
    result = await UserService().unassign_with_attribute(
        uow=uow, user_id=user_id, attr_id=attr_id
    )
    return result


@user_router.delete("/remove_assign_with_job")
async def unassign_with_job(uow: UOWDependence, user_id: UUID, job_id: UUID):
    result = await UserService().unassign_with_job(
        uow=uow, user_id=user_id, job_id=job_id
    )
    return result


@user_router.delete("/remove_user")
async def remove_user(uow: UOWDependence, user_id: UUID):
    result = await UserService().remove_user(uow=uow, user_id=user_id)
    return result
