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
    medical_book: Optional[bool] = False
    is_self_employed: Optional[bool] = False
    work_experience: Optional[str] = None
    activity_type: Optional[str] = None
    contraindications: Optional[str] = None
    about: Optional[str] = None
    education: Optional[str] = None
    driver_license: Optional[str] = None
    languages: Optional[str] = None
