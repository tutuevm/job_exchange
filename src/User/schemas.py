from pydantic import BaseModel, Field, EmailStr
from uuid import UUID, uuid4


class UserSchema(BaseModel):
    id : UUID = Field(default_factory=uuid4)
    full_name: str = Field(max_length=50)
    login: str = Field(max_length=50)
    email: EmailStr = Field(max_length=50)
    hashed_password: str

class ResponseUserSchema(BaseModel):
    id : UUID = Field(default_factory=uuid4)
    full_name: str = Field(max_length=50)
    login: str = Field(max_length=50)
    email: EmailStr = Field(max_length=50)

class UserInfo(BaseModel):
    id: UUID
    full_name: str
    login: str
    email: str
    is_active: bool