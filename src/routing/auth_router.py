from fastapi import APIRouter

from src.schemas.UserLoginShema import UserLoginSchema

auth_router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

@auth_router.post('/login')
def auth_user_issue_jwt(
        user: UserLoginSchema,
):
 ...