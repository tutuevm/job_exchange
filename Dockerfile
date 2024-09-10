FROM python:3.12.4-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    openssl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install poetry

ENV POETRY_VIRTUALENVS_CREATE=false
ENV PYTHONPATH=/job_exchange


COPY poetry.lock pyproject.toml /job_exchange/


WORKDIR /job_exchange
RUN poetry install --no-dev

COPY . /job_exchange

RUN mkdir -p /job_exchange/ssl
RUN openssl genrsa -out /job_exchange/crt/jwt-private.pem 2048 && \
    openssl rsa -in /job_exchange/crt/jwt-private.pem -outform PEM -pubout -out /job_exchange/crt/jwt-public.pem


WORKDIR /job_exchange/src

