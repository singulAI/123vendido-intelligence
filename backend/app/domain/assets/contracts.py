from enum import StrEnum
from pydantic import BaseModel, Field

class AssetKind(StrEnum):
    DOCUMENT = "document"
    IMAGE = "image"
    ATTACHMENT = "attachment"
    THUMBNAIL = "thumbnail"

class ProcessingStatus(StrEnum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"
    SKIPPED = "skipped"

class AssetMetadata(BaseModel):
    content_type: str | None = None
    size_bytes: int | None = Field(default=None, ge=0)
    width: int | None = None
    height: int | None = None
    pages: int | None = None
    checksum_sha256: str | None = None
    duplicate_of: str | None = None
    storage_provider: str = "local"
    bucket: str
    object_key: str
    ocr_status: ProcessingStatus = ProcessingStatus.PENDING
    ai_status: ProcessingStatus = ProcessingStatus.PENDING
    extra: dict = {}
