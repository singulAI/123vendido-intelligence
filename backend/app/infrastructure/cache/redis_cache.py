from typing import Protocol
import json
from redis.asyncio import Redis

class Cache(Protocol):
    async def get_json(self, key: str) -> dict | list | None: ...
    async def set_json(self, key: str, value: dict | list, ttl_seconds: int | None = None) -> None: ...
    async def delete(self, key: str) -> None: ...

class RedisCache:
    def __init__(self, redis: Redis):
        self.redis = redis
    async def get_json(self, key: str) -> dict | list | None:
        value = await self.redis.get(key)
        return json.loads(value) if value else None
    async def set_json(self, key: str, value: dict | list, ttl_seconds: int | None = None) -> None:
        await self.redis.set(key, json.dumps(value), ex=ttl_seconds)
    async def delete(self, key: str) -> None:
        await self.redis.delete(key)
