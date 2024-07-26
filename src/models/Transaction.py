from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import func, ForeignKey, Enum
from uuid import UUID, uuid4
from datetime import datetime, UTC
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.models.User import User

from src.database import Base
from src.schemas.TransactionSchema import TransactionStatus, TransactionType
class Transaction(Base):
    __tablename__ = 'user_transactions'

    id : Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), index=True)
    committed_at: Mapped[datetime] = mapped_column(
        server_default=func.timezone('UTC', func.now()),
        default=datetime.now(UTC),
    )
    amount: Mapped[int] = mapped_column(nullable=False)
    type: Mapped[str] = mapped_column(Enum(TransactionType), nullable=False)
    status: Mapped[str] = mapped_column(Enum(TransactionStatus), nullable=False)

