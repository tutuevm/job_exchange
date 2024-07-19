from pydantic import BaseModel, EmailStr


class UserLoginSchema(BaseModel):
    username : EmailStr | str
    password: str