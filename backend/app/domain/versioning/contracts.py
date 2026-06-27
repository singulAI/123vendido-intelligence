from enum import StrEnum
from pydantic import BaseModel

class VersionedResource(StrEnum):
    AUCTION_NOTICE = "auction_notice"
    LOT = "lot"
    VEHICLE = "vehicle"
    IMAGE = "image"
    SETTINGS = "settings"
    CONNECTOR = "connector"
    PLAN = "plan"
    PERMISSION = "permission"
    ANALYSIS = "analysis"

class VersionSnapshot(BaseModel):
    resource_type: VersionedResource
    resource_id: str
    version: int
    payload: dict
    changed_by: str | None = None
    change_reason: str | None = None
