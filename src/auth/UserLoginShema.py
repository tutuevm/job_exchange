from pydantic import BaseModel, EmailStr


class UserLoginSchema(BaseModel):
    username : EmailStr | str
    password: str

class TokenInfo(BaseModel):
    access_token: str
    token_type: str