from sqlalchemy import String
from uuid import UUID

from src.database import Base
from sqlalchemy.orm import Mapped, mapped_column



class Place(Base):
    __tablename__ = 'places'

    id: Mapped[UUID] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)

