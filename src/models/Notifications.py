from uuid import UUID, uuid4
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, func, ForeignKey
from datetime import datetime

from src.database import Base

class Notification(Base):
    __tablename__ = 'notifications'

    id : Mapped[UUID] = mapped_column(primary_key=True, default=uuid4())
    notification_data = mapped_column(String(400))
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        default=datetime.now(),
    )
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="notifications")