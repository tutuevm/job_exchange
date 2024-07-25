from pydantic import BaseModel
from enum import Enum



class TransactionStatus(Enum):
    COMPLETED = 'Выполнена'
    CANCELED = 'Отменена'
    PENDING = 'В ожидании'

class TransactionType(Enum):
    DEPOSIT = 'Пополнение'
    WITHDRAWAL = 'Снятие'