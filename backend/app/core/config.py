from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "123Vendido Intelligence API"
    api_prefix: str = "/api/v1"
    environment: str = "local"
    database_url: str = Field(default="postgresql+asyncpg://postgres:postgres@localhost:5432/123vendido")
    redis_url: str = "redis://localhost:6379/0"
    jwt_secret_key: str = "change-me"
    jwt_algorithm: str = "HS256"
    access_token_minutes: int = 30
    refresh_token_days: int = 30
    cors_origins: list[str] = ["http://localhost:5173", "http://localhost:3000"]
    model_config = SettingsConfigDict(env_file=".env", env_prefix="VENDIDO_", extra="ignore")

@lru_cache
def get_settings() -> Settings:
    return Settings()
