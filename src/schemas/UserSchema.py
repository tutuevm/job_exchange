from pydantic import BaseModel, Field, EmailStr
from uuid import UUID, uuid4


class UserSchema(BaseModel):
    id : UUID = Field(default_factory=uuid4)
    full_name: str = Field(max_length=50)
    email: EmailStr = Field(max_length=50)
    password: str


