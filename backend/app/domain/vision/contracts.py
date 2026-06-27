from typing import Protocol
from pydantic import BaseModel, Field
from app.domain.intelligence.contracts import LotAnalysisContext

class VisualAssessment(BaseModel):
    classification: str | None = None
    apparent_damage_hypotheses: list[str] = []
    preliminary_repair_estimate: dict = {}
    visual_score: float | None = Field(default=None, ge=0, le=100)
    confidence: float = Field(ge=0, le=1, default=0.0)
    limitations: list[str] = ["Contrato preparado; nenhuma inferência visual real implementada nesta fase."]

class VisionProvider(Protocol):
    async def analyze_images(self, context: LotAnalysisContext) -> VisualAssessment: ...
