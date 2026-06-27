from pydantic import BaseModel, Field
from app.domain.score.contracts import Score360

class DecisionInput(BaseModel):
    lot_id: str
    engine_outputs: dict = {}
    score_360: Score360
    constraints: dict = {}

class DecisionResult(BaseModel):
    lot_id: str
    final_decision_score: float = Field(ge=0, le=100)
    recommendation: str
    rationale: list[str] = []
    confidence: float = Field(ge=0, le=1)
    limitations: list[str] = []

class DecisionEngine:
    def decide(self, decision_input: DecisionInput) -> DecisionResult:
        score = decision_input.score_360.final_auction_score
        recommendation = "buy" if score >= 75 else "watch" if score >= 55 else "avoid"
        return DecisionResult(lot_id=decision_input.lot_id, final_decision_score=score, recommendation=recommendation, confidence=decision_input.score_360.confidence_score / 100, rationale=["Score 360 consolidado a partir dos engines independentes."])
