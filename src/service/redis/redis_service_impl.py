import json
from typing import List
from aioredis import Redis
from requests import delete
from service.redis.redis_service import RedisService


class RedisServiceImpl(RedisService):

    def __init__(self, redis_client: Redis):
        self.redis_client = redis_client

    async def get(self, key):
        print("dsdsds get!!z")
        return await self.redis_client.get(key)

    async def set(self, key: set, value: str, ttl: int = 3600000):
        print("set!")
        return await self.redis_client.set(key, json.dumps(value), ex=ttl)

    async def delete(self, key: str):
        print("dd")
