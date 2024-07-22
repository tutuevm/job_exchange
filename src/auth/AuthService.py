from datetime import datetime, UTC, timedelta

from fastapi import HTTPException

from src.auth.UserLoginShema import UserLoginSchema, TokenInfo
from src.utils.UnitOfWork import InterfaceUnitOfWork
from src.models.User import User
from src.auth.UserManager import UserManager
from src.config import settings
class AuthService:

    async def auth_user_issue_jwt(self, uow: InterfaceUnitOfWork, user: UserLoginSchema):
        user_login_data = user.model_dump()
        async with uow:
            user = await uow.user.get_users_by_different_fields(User.login ==user_login_data['username'],User.email==user_login_data['username'])
        if len(user) > 1:
            raise HTTPException(status_code=401, detail={"warning": "more than one user with the entered parameters was found"})

        if len(user) == 0:
            raise HTTPException(status_code=401, detail={"warning": "no users were found"})

        if not UserManager().validate_password(password=user_login_data['password'], hashed_password=user[0].hashed_password):
            raise HTTPException(status_code=401, detail={"warning": "wrong login or password"})

        return TokenInfo(
            access_token=UserManager().return_jwt(
                payload={
                    "sub": user[0].email,
                    "exp": datetime.now(UTC) + timedelta(minutes=settings.AUTH_SETTINGS.access_token_expire_minutes),
                }
            ),
            token_type="Bearer"
        )




    async def validate_user(self, username: str, password: str):
        ...
