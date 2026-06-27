from enum import StrEnum
from pydantic import BaseModel

class KnowledgeNodeType(StrEnum):
    ORGANIZER = "organizer"
    AUCTION = "auction"
    NOTICE = "notice"
    LOT = "lot"
    VEHICLE = "vehicle"
    IMAGE = "image"
    DOCUMENT = "document"
    ANALYSIS = "analysis"
    USER = "user"
    FAVORITE = "favorite"
    REPORT = "report"

class KnowledgeEdge(BaseModel):
    source_type: KnowledgeNodeType
    source_id: str
    relation: str
    target_type: KnowledgeNodeType
    target_id: str
    metadata: dict = {}
