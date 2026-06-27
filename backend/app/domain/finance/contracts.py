from pydantic import BaseModel

class FinancialInputs(BaseModel):
    fipe_price_cents: int | None = None
    market_price_cents: int | None = None
    notice_value_cents: int
    estimated_cost_cents: int = 0
    taxes_cents: int = 0
    freight_cents: int = 0
    commission_cents: int = 0
    documentation_cents: int = 0

class FinancialResult(BaseModel):
    margin_cents: int
    profit_cents: int
    roi_percent: float
    payback_days: int | None = None
    score: float

def calculate_financial_result(inputs: FinancialInputs) -> FinancialResult:
    reference_price = inputs.market_price_cents or inputs.fipe_price_cents or inputs.notice_value_cents
    total_cost = inputs.notice_value_cents + inputs.estimated_cost_cents + inputs.taxes_cents + inputs.freight_cents + inputs.commission_cents + inputs.documentation_cents
    profit = reference_price - total_cost
    roi = (profit / total_cost * 100) if total_cost else 0
    score = max(0, min(100, 50 + roi))
    return FinancialResult(margin_cents=reference_price - inputs.notice_value_cents, profit_cents=profit, roi_percent=roi, score=score)
