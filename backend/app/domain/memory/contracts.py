from pydantic import BaseModel

class AIMemoryEntry(BaseModel):
    prompt: str
    response: str
    user_feedback: str | None = None
    correction: str | None = None
    learning: dict = {}
    history_entry_id: str | None = None
