from abc import ABCMeta, abstractmethod
from typing import List


class RedisService(metaclass=ABCMeta):
    @abstractmethod
    async def set(self, key: str, value: str, ttl: int = 3600):
        pass

    @abstractmethod
    async def get(self, key):
        pass

    @abstractmethod
    async def delete(self, key: str):
        pass
