import os

from pydantic_settings import  BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    API_TITLE : str = os.environ.get('API_TITLE')
    API_DESCRIPTION: str = os.environ.get('API_DESCRIPTION')
    API_VERSION: str = os.environ.get('API_VERSION')


class DataBaseSettings(BaseSettings):
    DATABASE_USER: str = os.environ.get('DATABASE_USER')
    DATABASE_PASSWORD: str = os.environ.get('DATABASE_PASSWORD')
    DB_HOST: str = os.environ.get('DB_HOST')
    DB_PORT: str = os.environ.get('DB_PORT')


settings = Settings()

db_settings = DataBaseSettings
