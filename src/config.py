import logging
import os
from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_settings import BaseSettings

load_dotenv()

BASE_DIR = Path(__file__).parent.parent


class AuthSettings(BaseModel):
    algorithm: str = "RS256"
    access_token_expire_minutes: int = 60 * 24
    refresh_token_expire_days: int = 30


class SSLSettings(BaseModel):
    private_jwt_key: Path = BASE_DIR / "crt" / "jwt-private.pem"
    public_jwt_key: Path = BASE_DIR / "crt" / "jwt-public.pem"


class DataBaseSettings(BaseModel):
    DB_USER: str = os.environ.get("DATABASE_USER")
    DB_PASSWORD: str = os.environ.get("DATABASE_PASSWORD")
    DB_NAME: str = os.environ.get("DB_NAME")
    DB_HOST: str = os.environ.get("DB_HOST")
    DB_PORT: str = os.environ.get("DB_PORT")


class Settings(BaseSettings):
    API_TITLE: str = os.environ.get("API_TITLE")
    API_DESCRIPTION: str = os.environ.get("API_DESCRIPTION")
    API_VERSION: str = os.environ.get("API_VERSION")
    DB_SETTINGS: DataBaseSettings = DataBaseSettings()
    SSL_Settings: SSLSettings = SSLSettings()
    AUTH_SETTINGS: AuthSettings = AuthSettings()


log = logging.getLogger()

settings = Settings()
