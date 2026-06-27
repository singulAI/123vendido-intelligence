from typing import Protocol
from pydantic import BaseModel, Field

class InformationSource(BaseModel):
    field: str
    origin: str
    confidence: float = Field(ge=0, le=1)

class LotAnalysisContext(BaseModel):
    structured_data: dict = {}
    notice: dict | None = None
    lot: dict = {}
    vehicle: dict | None = None
    images: list[dict] = []
    official_url: str | None = None
    user_observations: dict = {}
    known_information: dict = {}
    history: list[dict] = []
    sources: list[InformationSource] = []

class EngineResult(BaseModel):
    engine: str
    version: int = 1
    score: float | None = None
    result: dict = {}
    confidence: float = Field(ge=0, le=1, default=0.5)
    limitations: list[str] = ["Mock provider; estimativas probabilísticas dependem da qualidade dos dados disponíveis."]

class IntelligenceEngine(Protocol):
    name: str
    async def analyze(self, context: LotAnalysisContext) -> EngineResult: ...
