from typing import Any
from pydantic import BaseModel

class ApiResponse(BaseModel):
    success: bool = True
    data: Any = None
    meta: dict = {}
    errors: list[dict] = []

class PageMeta(BaseModel):
    page: int = 1
    per_page: int = 20
    total: int = 0
