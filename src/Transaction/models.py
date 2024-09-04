from datetime import datetime, UTC
from uuid import UUID, uuid4

from sqlalchemy import func, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column

from src.Transaction.schemas import TransactionStatus, TransactionType
from src.database import Base


class Transaction(Base):
    __tablename__ = "user_transactions"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), index=True)
    committed_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        default=datetime.now(UTC).replace(tzinfo=None),
    )
    amount: Mapped[int] = mapped_column(nullable=False)
    type: Mapped[str] = mapped_column(Enum(TransactionType), nullable=False)
    status: Mapped[str] = mapped_column(Enum(TransactionStatus), nullable=False)
