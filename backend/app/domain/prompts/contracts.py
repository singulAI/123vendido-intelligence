from pydantic import BaseModel, Field
from app.domain.ai.contracts import AIProvider

class PromptTemplate(BaseModel):
    key: str
    version: int = 1
    provider: AIProvider | None = None
    template: str
    variables: list[str] = []
    temperature: float = Field(default=0.2, ge=0, le=2)
    max_tokens: int | None = None
    fallback_template_key: str | None = None

class PromptTestCase(BaseModel):
    prompt_key: str
    input_variables: dict
    expected_assertions: list[str] = []
