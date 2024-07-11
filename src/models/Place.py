from sqlalchemy import String

from src.database import Base
from sqlalchemy.orm import Mapped, mapped_column



class Place(Base):
    __tabelname__ = 'place'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)

