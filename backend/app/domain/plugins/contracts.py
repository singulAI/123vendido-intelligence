from enum import StrEnum
from pydantic import BaseModel

class PluginKind(StrEnum):
    CONNECTOR = "connector"
    AI_PROVIDER = "ai_provider"
    BILLING = "billing"
    MAPS = "maps"
    STORAGE = "storage"
    IDENTITY = "identity"
    GOVERNMENT_API = "government_api"

class PluginManifest(BaseModel):
    key: str
    kind: PluginKind
    version: str
    enabled: bool = False
    configuration_schema: dict = {}
    healthcheck_path: str | None = None
