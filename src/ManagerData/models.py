from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base

if TYPE_CHECKING:
    from src.User.models import User


class ManagerData(Base):
    __tablename__ = "manager_data"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    surname: Mapped[str] = mapped_column(String(50), nullable=False)
    patronymic: Mapped[str] = mapped_column(String(50), nullable=False)
    job_title: Mapped[str] = mapped_column(String(50), nullable=False)
    work_phone: Mapped[str] = mapped_column(String(15), nullable=False)
    organization: Mapped["UUID"] = mapped_column(ForeignKey("organizations.id"))
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), index=True)

    user: Mapped["User"] = relationship(back_populates="manager_data")
