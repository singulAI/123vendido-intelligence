from enum import StrEnum
from pydantic import BaseModel, Field

class AIProvider(StrEnum):
    OPENAI = "openai"
    CLAUDE = "claude"
    GEMINI = "gemini"
    DEEPSEEK = "deepseek"
    QWEN = "qwen"
    LLAMA = "llama"
    MISTRAL = "mistral"
    OLLAMA = "ollama"
    CUSTOM = "custom_models"

class ModelSelectorPolicy(BaseModel):
    preferred_provider: AIProvider | None = None
    allowed_providers: list[AIProvider] = []
    max_cost_cents: int | None = None
    max_latency_ms: int | None = None
    fallback_chain: list[AIProvider] = []
    rate_limit_key: str | None = None

class AIRequest(BaseModel):
    prompt_template_key: str
    variables: dict = {}
    policy: ModelSelectorPolicy = Field(default_factory=ModelSelectorPolicy)
