from app.domain.intelligence.contracts import EngineResult, LotAnalysisContext

class MockIntelligenceEngine:
    def __init__(self, name: str):
        self.name = name
    async def analyze(self, context: LotAnalysisContext) -> EngineResult:
        return EngineResult(engine=self.name, score=50.0, result={"context_keys": list(context.model_dump().keys())})

ENGINE_NAMES = ["valuation", "cost", "profitability", "opportunity", "recommendation", "risk", "market_intelligence", "liquidity", "simulation", "ai_insight"]
