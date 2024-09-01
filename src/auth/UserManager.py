from abc import ABC, abstractmethod
from typing import Dict

import bcrypt
import jwt
from fastapi import Depends, status, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jwt import ExpiredSignatureError

from src.config import settings


class IUserManager(ABC):
    http_bearer = HTTPBearer()

    @abstractmethod
    def hash_password(self, password: str) -> bytes:
        raise NotImplementedError

    @abstractmethod
    def validate_password(self, password: str, hashed_password: bytes) -> bool:
        raise NotImplementedError

    @abstractmethod
    def return_jwt(self, payload: Dict, key: str, algorithm: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def check_jwt(self, token: str, public_key: str, algorithm: str) -> Dict:
        raise NotImplementedError

    @abstractmethod
    def get_current_auth_user_payload(
        self, cred: HTTPAuthorizationCredentials = Depends(HTTPBearer)
    ):
        raise NotImplementedError


class UserManager(IUserManager):
    http_bearer = HTTPBearer()

    def hash_password(self, password) -> bytes:
        salt = bcrypt.gensalt()
        pwd_bytes: bytes = password.encode()
        return bcrypt.hashpw(pwd_bytes, salt)

    def validate_password(self, password: str, hashed_password: bytes) -> bool:
        return bcrypt.checkpw(password.encode(), hashed_password)

    def return_jwt(
        self,
        payload: dict,
        key=settings.SSL_Settings.private_jwt_key.read_text(),
        algorithm=settings.AUTH_SETTINGS.algorithm,
    ):
        return jwt.encode(payload, key, algorithm=algorithm)

    def check_jwt(
        self,
        token: str,
        public_key=settings.SSL_Settings.public_jwt_key.read_text(),
        algorithm=settings.AUTH_SETTINGS.algorithm,
    ):
        return jwt.decode(jwt=token, key=public_key, algorithms=[algorithm])

    def get_current_auth_user_payload(
        self, cred: HTTPAuthorizationCredentials = Depends(http_bearer)
    ):
        token = cred.credentials
        try:
            return self.check_jwt(token=token)
        except ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Signature has expired"
            )
        except Exception as e:
            print(e)
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="something wrong"
            )
