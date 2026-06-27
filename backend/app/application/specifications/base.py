from dataclasses import dataclass, field
from typing import Any

@dataclass(frozen=True)
class FilterCondition:
    field: str
    operator: str
    value: Any

@dataclass(frozen=True)
class SortCondition:
    field: str
    descending: bool = False

@dataclass(frozen=True)
class Specification:
    filters: tuple[FilterCondition, ...] = field(default_factory=tuple)
    sorts: tuple[SortCondition, ...] = field(default_factory=tuple)
    page: int = 1
    per_page: int = 20
    include_deleted: bool = False

    def where(self, field: str, operator: str, value: Any) -> "Specification":
        return Specification(self.filters + (FilterCondition(field, operator, value),), self.sorts, self.page, self.per_page, self.include_deleted)

    def order_by(self, field: str, descending: bool = False) -> "Specification":
        return Specification(self.filters, self.sorts + (SortCondition(field, descending),), self.page, self.per_page, self.include_deleted)
