from pydantic import BaseModel, EmailStr
from uuid import UUID

class UserLoginSchema(BaseModel):
    username : EmailStr | str
    password: str

class TokenInfo(BaseModel):
    access_token: str
    refresh_token: str | None = None
    token_type: str
    user : UUID | None = None