from sqlalchemy import select, or_
from sqlalchemy.orm import selectinload
from fastapi import HTTPException, status

from src.utils.repository import SQLAlchemyRepository
from src.models.Transaction import Transaction




class TransactionRepository(SQLAlchemyRepository):
    model = Transaction