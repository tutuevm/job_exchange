from uuid import UUID

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base


class UserAttribute(Base):
    __tablename__ = "user_attributes"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    key: Mapped[str] = mapped_column(String(50), nullable=False)
    value: Mapped[str] = mapped_column(String(50), nullable=False)

    user = relationship(
        "User", secondary="user_attribute_association", back_populates="attributes"
    )
