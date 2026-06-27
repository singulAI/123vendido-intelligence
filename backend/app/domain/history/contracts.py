from enum import StrEnum
from pydantic import BaseModel

class HistoryKind(StrEnum):
    ANALYSIS = "analysis"
    QUERY = "query"
    CHANGE = "change"
    AI_USAGE = "ai_usage"
    PROMPT = "prompt"
    SCORE = "score"
    DECISION = "decision"
    CALCULATION = "calculation"

class HistoryEntry(BaseModel):
    kind: HistoryKind
    actor_id: str | None = None
    resource_type: str
    resource_id: str
    payload: dict = {}
    correlation_id: str | None = None
