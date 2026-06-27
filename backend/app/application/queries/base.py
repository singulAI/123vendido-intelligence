from dataclasses import dataclass

@dataclass(frozen=True)
class PageQuery:
    page: int = 1
    per_page: int = 20
    search: str | None = None
    sort: str | None = None

@dataclass(frozen=True)
class LotSearchQuery(PageQuery):
    organizer_id: str | None = None
    auction_id: str | None = None
    make: str | None = None
    model: str | None = None
    min_score: float | None = None
    max_price_cents: int | None = None
    region: str | None = None
