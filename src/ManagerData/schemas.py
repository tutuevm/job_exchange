from uuid import UUID

from pydantic import BaseModel, Field


class ManagerDataCreateSchema(BaseModel):
    name: str = Field(max_length=50)
    surname: str = Field(max_length=50)
    patronymic: str = Field(max_length=50)
    job_title: str = Field(max_length=50)
    work_phone: str = Field(max_length=15)
    organization: UUID
    user_id: UUID


class UserDataUpdateSchema(BaseModel):
    user_id: UUID
    update_data: dict
