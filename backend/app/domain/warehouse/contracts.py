from enum import StrEnum
from pydantic import BaseModel

class WarehouseLayer(StrEnum):
    OPERATIONAL_DATABASE = "operational_database"
    DATA_LAKE = "data_lake"
    DATA_WAREHOUSE = "data_warehouse"
    ANALYTICS = "analytics"
    DASHBOARD = "dashboard"

class WarehouseDataset(BaseModel):
    name: str
    layer: WarehouseLayer
    source: str
    refresh_policy: str = "daily"
    schema_version: int = 1
