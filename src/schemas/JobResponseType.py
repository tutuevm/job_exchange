from enum import Enum


class JobResponseType(Enum):
    SUBMITTED = 'Отправлен'
    UNDER_REVIEW = 'На рассмотрении'
    ACCEPTED = 'Принят'
    REJECTED = 'Отклонен'
    WITHDRAWN = 'Отозван'