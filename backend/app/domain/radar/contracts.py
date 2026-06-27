from enum import StrEnum
from pydantic import BaseModel

class AlertKind(StrEnum):
    PRICE = "price_alert"
    ORGANIZER = "organizer_alert"
    VEHICLE = "vehicle_alert"
    KEYWORD = "keyword_alert"

class SavedSearch(BaseModel):
    name: str
    keywords: list[str] = []
    regions: list[str] = []
    categories: list[str] = []
    max_price_cents: int | None = None
    organizers: list[str] = []
    vehicles: list[str] = []

class Watchlist(BaseModel):
    user_id: str
    saved_searches: list[SavedSearch] = []
    alert_kinds: list[AlertKind] = []
