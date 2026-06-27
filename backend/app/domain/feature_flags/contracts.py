from enum import StrEnum
from pydantic import BaseModel

class FeatureKey(StrEnum):
    VISION_AI = "vision_ai"
    OCR = "ocr"
    PARSER = "parser"
    RADAR = "radar"
    MARKETPLACE = "marketplace"
    CRAWLER = "crawler"
    SCRAPERS = "scrapers"
    OPENAI = "openai"
    OLLAMA = "ollama"
    MISTRAL = "mistral"
    BILLING = "billing"
    DEVELOPER_CENTER = "developer_center"

class FeatureFlag(BaseModel):
    key: FeatureKey
    enabled: bool = False
    rollout_percentage: int = 0
    rules: dict = {}
