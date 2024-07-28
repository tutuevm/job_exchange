from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse

from src.auth.UserLoginShema import UserLoginSchema, TokenInfo
from src.depends import UOWDependence, UserManagerDependence, UserPayloadDependence
from src.auth.AuthService import AuthService

auth_router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

@auth_router.post('/login', response_model=TokenInfo)
async def auth_user_issue_jwt(
        manager: UserManagerDependence,
        user_data: UserLoginSchema,
        uow: UOWDependence
):
    try:
        result = await AuthService().auth_user_issue_jwt( uow=uow, manager=manager, user=user_data)
        return result
    except HTTPException as e:
        return JSONResponse(status_code=e.status_code, content=e.detail)

@auth_router.post('/check_jwt')
async def check_jwt(
        manager: UserManagerDependence,
        jwt: str
):
    try:
        return await AuthService().validate_jwt(manager=manager, jwt=jwt)
    except HTTPException as e:
        return JSONResponse(status_code=e.status_code, content=e.detail)

@auth_router.post('/check_user')
async def check_jwt(
        uow: UOWDependence,
        payload: UserPayloadDependence
):
    return await AuthService().get_current_auth_user(uow=uow, payload=payload)