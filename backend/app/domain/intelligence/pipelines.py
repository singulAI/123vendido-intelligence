from enum import StrEnum
from typing import Protocol
from app.domain.intelligence.contracts import EngineResult, LotAnalysisContext

class IntelligencePipeline(StrEnum):
    MARKET = "market_intelligence"
    OPPORTUNITY = "opportunity_engine"
    RISK = "risk_engine"
    REPAIR_COST = "repair_cost_engine"
    LIQUIDITY = "liquidity_engine"
    PRICING = "pricing_engine"
    RECOMMENDATION = "recommendation_engine"
    VISION = "vision_engine"
    DOCUMENT = "document_intelligence"
    AI_ORCHESTRATOR = "ai_orchestrator"
    KNOWLEDGE_GRAPH = "knowledge_graph"

class PipelineEngine(Protocol):
    pipeline: IntelligencePipeline
    async def run(self, context: LotAnalysisContext) -> EngineResult: ...

PIPELINE_ORDER = [
    IntelligencePipeline.DOCUMENT,
    IntelligencePipeline.VISION,
    IntelligencePipeline.MARKET,
    IntelligencePipeline.PRICING,
    IntelligencePipeline.REPAIR_COST,
    IntelligencePipeline.RISK,
    IntelligencePipeline.LIQUIDITY,
    IntelligencePipeline.OPPORTUNITY,
    IntelligencePipeline.RECOMMENDATION,
    IntelligencePipeline.AI_ORCHESTRATOR,
    IntelligencePipeline.KNOWLEDGE_GRAPH,
]
