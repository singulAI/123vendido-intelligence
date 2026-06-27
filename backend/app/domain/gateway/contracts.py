from pydantic import BaseModel

class GatewayRoute(BaseModel):
    path: str
    requires_auth: bool = True
    rate_limit_per_minute: int | None = None
    cache_ttl_seconds: int | None = None
    supports_rest: bool = True
    future_graphql: bool = False
    future_websocket: bool = False
