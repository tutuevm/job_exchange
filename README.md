# Job Exchange

Job Exchange is a web application designed to facilitate job postings and applications. Built using FastAPI and SQLAlchemy, it allows users to create job listings, apply for jobs, and manage their applications.

## Table of Contents
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [Configuration](#configuration)
- [Environment Variables](#environment-variables)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites
- Python 3.7+
- `Poetry` (Python dependency management and packaging tool)

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/tutuevm/job_exchange.git
    cd job_exchange
    ```

2. Install the dependencies using Poetry:
    ```bash
    poetry install
    ```

3. Activate the virtual environment created by Poetry:
    ```bash
    poetry shell
    ```

## Running the Application
1. Start the FastAPI application:
    ```bash
    uvicorn src.main:app --reload
    ```

By default, the application will be accessible at `http://127.0.0.1:8000`.

2. (Optional) Configure the host and port if needed:
    ```bash
    uvicorn src.main:app --host 0.0.0.0 --port 8080 --reload
    ```

## API Documentation
FastAPI provides interactive API documentation. You can access it at:
- Swagger UI: `http://127.0.0.1:8000/docs`

## Configuration
Configuration details for the application, including environment variables and other settings:
- `DATABASE_URL`: Database connection URL
- `SECRET_KEY`: Secret key for authentication

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
