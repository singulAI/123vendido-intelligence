from pydantic import BaseModel
from app.domain.intelligence.contracts import LotAnalysisContext

class AIContextBuilderInput(BaseModel):
    vehicle: dict = {}
    notice: dict = {}
    lot: dict = {}
    organizer: dict = {}
    observations: dict = {}
    history: list[dict] = []
    market: dict = {}
    images: list[dict] = []

class AIContextBuilder:
    def build(self, source: AIContextBuilderInput) -> LotAnalysisContext:
        return LotAnalysisContext(structured_data={"organizer": source.organizer, "market": source.market}, notice=source.notice, lot=source.lot, vehicle=source.vehicle, images=source.images, user_observations=source.observations, history=source.history, sources=[{"field": "context", "origin": "ai_context_builder", "confidence": 1.0}])
