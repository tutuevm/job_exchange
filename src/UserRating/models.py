from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import ForeignKey, func, String
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class UserRating(Base):
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    rated_by: Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    rating_value: Mapped[float] = mapped_column(nullable=False)
    comment: Mapped[str] = mapped_column(String(100), nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        default=datetime.now,
    )
