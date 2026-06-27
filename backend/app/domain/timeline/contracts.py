from enum import StrEnum
from pydantic import BaseModel

class TimelineEventType(StrEnum):
    NOTICE_PUBLISHED = "notice_published"
    LOT_IMPORTED = "lot_imported"
    IMAGES_RECEIVED = "images_received"
    AI_EXECUTED = "ai_executed"
    USER_FAVORITED = "user_favorited"
    NEW_ANALYSIS = "new_analysis"
    MARKET_CHANGED = "market_changed"
    FIPE_CHANGED = "fipe_changed"
    NEW_SCORE = "new_score"

class TimelineEvent(BaseModel):
    lot_id: str
    event_type: TimelineEventType
    payload: dict = {}
    correlation_id: str | None = None
