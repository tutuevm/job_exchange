from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from uuid import UUID

from src.database import Base


class Organization(Base):
    __tablename__ = 'organizations'

    id: Mapped[UUID] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))

