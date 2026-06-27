from pydantic import BaseModel

class EmbeddingRecord(BaseModel):
    resource_type: str
    resource_id: str
    vector_provider: str = "mock"
    embedding_model: str = "mock-embedding"
    dimensions: int = 0
    metadata: dict = {}

class SemanticSearchQuery(BaseModel):
    query: str
    top_k: int = 10
    filters: dict = {}
