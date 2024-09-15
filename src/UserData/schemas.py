from typing import Optional

from pydantic import BaseModel, Field
from datetime import date


class UserDataCreatedSchema(BaseModel):
    name: str
    surname: str
    patronymic: str
    date_of_birth: date
    phone_number: str
    citizenship: str
    city: str
    passport_data: str = Field(min_length=10, max_length=10)
    snils: str = Field(max_length=11, min_length=11)
    medical_book: bool
    is_self_employed: bool
    work_experience: str = Field(default=None)
    activity_type: str = Field(default=None)
    contraindications: str = Field(default=None)
    about: str = Field(default=None)
    education: str = Field(default=None)
    driver_license: str = None
    languages: Optional[str] = None
