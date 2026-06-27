from enum import StrEnum
from pydantic import BaseModel

class DataLakeStage(StrEnum):
    RAW = "raw_data"
    NORMALIZED = "normalized_data"
    VALIDATED = "validated_data"
    ENRICHED = "enriched_data"
    AI = "ai_data"
    USER = "user_data"

IMMUTABLE_STAGES = [DataLakeStage.RAW]

class DataLakeRecord(BaseModel):
    source_type: str
    source_id: str
    stage: DataLakeStage
    version: int = 1
    payload: dict
    parent_record_id: str | None = None
    immutable: bool = False
