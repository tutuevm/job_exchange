# Используем официальный образ Python
FROM python:3.12.4-slim

# Устанавливаем зависимости для сборки
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем Poetry
RUN pip install poetry

# Устанавливаем переменную окружения, чтобы Poetry не создавала виртуальное окружение
ENV POETRY_VIRTUALENVS_CREATE=false
ENV PYTHONPATH=/job_exchange
# Копируем файлы Poetry для установки зависимостей
COPY poetry.lock pyproject.toml /job_exchange/

# Устанавливаем зависимости
WORKDIR /job_exchange
RUN poetry install --no-dev

# Копируем все файлы приложения
COPY . /job_exchange

# Указываем рабочую директорию на src
WORKDIR /job_exchange/src

# Запуск через модульный импорт

CMD ["python", "-m", "main"]
