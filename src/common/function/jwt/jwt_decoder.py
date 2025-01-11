import os
from abc import ABC, abstractmethod
from jose import ExpiredSignatureError, jwt


class AbstractJWTDecoder(ABC):

    @abstractmethod
    def decode(self, token: str, secret_key: str, algorithm: str) -> dict | None:
        pass


class JWTDecoder(AbstractJWTDecoder):
    def __init__(self):
        self.secret_key = os.getenv("JWT_SECRET_KEY")
        self.algorithm = os.getenv("JWT_ALGORITHM")

    def decode(self, token: str):
        try:
            return jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
        except ExpiredSignatureError:
            # 유효기간이 지난 경우
            print("Token has expired.")
            return None
        except:
            return None
