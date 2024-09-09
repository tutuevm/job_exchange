# Job Exchange

Job Exchange is a web application designed to facilitate job postings and applications. Built using FastAPI and
SQLAlchemy, it allows users to create job listings, apply for jobs, and manage their applications.

## Table of Contents

- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [Configuration](#configuration)
- [Environment Variables](#environment-variables)
- [Testing](#testing)

## Installation

### Prerequisites

- Docker

### Steps

1. Update and rename .env and .test-env files


2. Running the Application in container:
    ```bash
      docker compose up --build
    ```

## API Documentation

FastAPI provides interactive API documentation. You can access it at:

- Swagger UI: `http://127.0.0.1:8010/docs`

## Environment Variables

The application uses the following environment variables:

- `API_TITLE`: Title of the API
- `API_DESCRIPTION`: Description of the API
- `API_VERSION`: Version of the API
- `DATABASE_USER`: Database username
- `DATABASE_PASSWORD`: Database password
- `DB_HOST`: Database host
- `DB_PORT`: Database port
- `DB_NAME`: Database name

## Testing

To run tests, use:

```bash
pytest
