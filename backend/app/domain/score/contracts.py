from pydantic import BaseModel, Field

class Score360(BaseModel):
    opportunity_score: float = Field(ge=0, le=100)
    risk_score: float = Field(ge=0, le=100)
    repair_score: float = Field(ge=0, le=100)
    market_score: float = Field(ge=0, le=100)
    liquidity_score: float = Field(ge=0, le=100)
    roi_score: float = Field(ge=0, le=100)
    confidence_score: float = Field(ge=0, le=100)
    final_auction_score: float = Field(ge=0, le=100)

    @classmethod
    def weighted(cls, **scores: float) -> "Score360":
        final = (scores["opportunity_score"] * 0.2 + (100 - scores["risk_score"]) * 0.15 + scores["repair_score"] * 0.1 + scores["market_score"] * 0.15 + scores["liquidity_score"] * 0.1 + scores["roi_score"] * 0.2 + scores["confidence_score"] * 0.1)
        return cls(final_auction_score=max(0, min(100, final)), **scores)
