from src.Transaction.models import Transaction
from src.utils.repository import SQLAlchemyRepository


class TransactionRepository(SQLAlchemyRepository):
    model = Transaction
