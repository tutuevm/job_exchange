from uuid import UUID

from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped

from src.database import Base


class ActionType(Base):

    __tablename__ = "action_types"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50), nullable=False)
