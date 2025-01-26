from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from jose import jwt, JWTError


class AbstractJWTEncoder(ABC):

    @abstractmethod
    def encode(self, data: dict, expires_delta: int, secret_key: str, algorithm: str):
        pass


class JWTEncoder(AbstractJWTEncoder):
    def encode(self, data, expires_delta, secret_key, algorithm):
        to_encode = data.copy()
        expire = datetime.now(ZoneInfo("Asia/Seoul")) + timedelta(minutes=expires_delta)
        to_encode.update({"exp": int(expire.timestamp())})
        return jwt.encode(to_encode, secret_key, algorithm=algorithm)
