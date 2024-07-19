from src.schemas.UserLoginShema import UserLoginSchema


class AuthService:

    async def auth_user_issue_jwt(self, user: UserLoginSchema):
        user_login_data = user.model_dump()


    async def validate_user(self, username: str, password: str):
        ...
