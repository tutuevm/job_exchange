from datetime import datetime, UTC, timedelta

from fastapi import HTTPException, status
from jwt import ExpiredSignatureError, InvalidSignatureError

from src.auth.UserLoginShema import UserLoginSchema, TokenInfo
from src.utils.UnitOfWork import InterfaceUnitOfWork
from src.models.User import User
from src.auth.UserManager import IUserManager
from src.config import settings


class AuthService:

    async def auth_user_issue_jwt(self, uow: InterfaceUnitOfWork, manager: IUserManager, user: UserLoginSchema):
        user_login_data = user.model_dump()
        async with uow:
            user = await uow.user.get_users_by_different_fields(User.login == user_login_data['username'],
                                                                User.email == user_login_data['username'])
        if len(user) > 1:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail={"warning": "more than one user with the entered parameters was found"})

        if len(user) == 0:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail={"warning": "no users were found"})

        if not manager.validate_password(password=user_login_data['password'], hashed_password=user[0].hashed_password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail={"warning": "wrong login or password"})

        return TokenInfo(
            access_token=manager.return_jwt(
                payload={
                    "type": 'access',
                    "sub": user[0].email,
                    "exp": datetime.now(UTC) + timedelta(minutes=settings.AUTH_SETTINGS.access_token_expire_minutes),
                }
            ),
            token_type="Bearer",
            refresh_token = manager.return_jwt(
                payload={
                    "type": 'refresh',
                    "sub": user[0].email,
                    "exp": datetime.now(UTC) + timedelta(minutes=settings.AUTH_SETTINGS.access_token_expire_minutes),
                }
            ),
            user=user[0].id
        )

    async def validate_jwt(self, manager: IUserManager, jwt: str):
        try:
            return manager.check_jwt(token=jwt)
        except ExpiredSignatureError:
            raise HTTPException(status_code=401, detail={'warning': 'ExpiredSignatureError'})
        except InvalidSignatureError:
            raise HTTPException(status_code=401, detail={'warning': 'InvalidSignatureError'})

    async def get_current_auth_user(self, uow: InterfaceUnitOfWork, payload):
        if payload['type'] != 'access':
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='invalid token type'
            )
        user_email = payload['sub']
        async with uow:
            user = await uow.user.find_by_filter(email=user_email)
        return {
            'id' : user[0].id,
            'username' : user[0].login
        }

    async def refresh_auth_cuurent_user(self,manager:IUserManager, payload) -> TokenInfo:
        if payload['type'] != 'refresh':
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='invalid token type'
            )
        return TokenInfo(
            access_token=manager.return_jwt(
                payload={
                    "type": 'access',
                    "sub": payload['sub'],
                    "exp": datetime.now(UTC) + timedelta(minutes=settings.AUTH_SETTINGS.refresh_token_expire_days),
                }
            ),
            token_type="Bearer",
        )