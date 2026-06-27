from typing import Protocol
from pydantic import BaseModel

class ConnectorConfig(BaseModel):
    provider: str
    version: str = "mock"
    credentials_ref: str | None = None
    timeout_seconds: int = 30
    retry_policy: dict = {"max_attempts": 3, "backoff": "exponential"}

class ConnectorHealth(BaseModel):
    provider: str
    healthy: bool
    latency_ms: int | None = None
    details: dict = {}

class ConnectorProvider(Protocol):
    config: ConnectorConfig
    async def health_check(self) -> ConnectorHealth: ...
