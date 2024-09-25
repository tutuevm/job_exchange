from datetime import date
from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import String, Date, CHAR, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base

if TYPE_CHECKING:
    from src.User.models import User


class UserData(Base):
    __tablename__ = "user_data"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), index=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    surname: Mapped[str] = mapped_column(String(50), nullable=False)
    patronymic: Mapped[str] = mapped_column(String(50), nullable=False)
    date_of_birth: Mapped[date] = mapped_column(Date)
    phone_number: Mapped[str] = mapped_column(String)
    citizenship: Mapped[str] = mapped_column(String(50), nullable=False)
    city: Mapped[str] = mapped_column(String(100))

    passport_data: Mapped[str] = mapped_column(CHAR(10), nullable=False)
    snils: Mapped[str] = mapped_column(CHAR(11), nullable=False)
    medical_book: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_self_employed: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )

    work_experience: Mapped[str | None] = mapped_column(String(400), nullable=True)
    activity_type: Mapped[str | None] = mapped_column(String(50), nullable=True)
    contraindications: Mapped[str | None] = mapped_column(String(200), nullable=True)

    about: Mapped[str | None] = mapped_column(String(400), nullable=True)
    education: Mapped[str | None] = mapped_column(String(400), nullable=True)
    driver_license: Mapped[str | None] = mapped_column(String(100), nullable=True)
    languages: Mapped[str | None] = mapped_column(String(200), nullable=True)

    user: Mapped["User"] = relationship(back_populates="user_data")
