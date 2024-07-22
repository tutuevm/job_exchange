from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from src.auth.UserLoginShema import UserLoginSchema, TokenInfo
from src.depends import UOWDependence
from src.auth.AuthService import AuthService

auth_router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

@auth_router.post('/login', response_model=TokenInfo)
async def auth_user_issue_jwt(
        user_data: UserLoginSchema,
        uow: UOWDependence
):
    try:
        result = await AuthService().auth_user_issue_jwt(uow=uow, user=user_data)
        return result
    except HTTPException as e:
        return JSONResponse(status_code=e.status_code, content=e.detail)