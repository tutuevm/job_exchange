import bcrypt
import jwt

from src.config import settings


class UserManager:

    def hash_password(self, password) -> bytes:
        salt = bcrypt.gensalt()
        pwd_bytes: bytes = password.encode()
        return bcrypt.hashpw(pwd_bytes, salt)

    def validate_password(self, password, hashed_password) -> bool:
        return bcrypt.checkpw(password.encode(), hashed_password)

    def return_jwt(
            self,
            payload: dict,
            key=settings.SSL_Settings.private_jwt_key.read_text(),
            algorithm=settings.AUTH_SETTINGS.algorithm
    ):
        return jwt.encode(payload, key, algorithm=algorithm)

    def check_jwt(
            self,
            token: str | bytes,
            public_key=settings.SSL_Settings.public_jwt_key.read_text(),
            algorithm=settings.AUTH_SETTINGS.algorithm
    ):
        return jwt.decode(jwt=token, key=public_key, algorithms=[algorithm])
