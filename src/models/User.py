from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey, String
from uuid import UUID
from typing import List

from src.database import Base



class User(Base):
    __tablename__ = "user"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    attributes: Mapped[List["Child"]] = mapped_column(ForeignKey("role.id"))
    full_name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50))
    hashed_password: Mapped[str] = mapped_column(String(128))
    assigned_jobs = relationship("JobResponse", back_populates = 'user')


