from enum import StrEnum
from pydantic import BaseModel

class ProcessingStep(StrEnum):
    UPLOAD = "upload"
    VALIDATION = "validation"
    EXTRACTION = "extraction"
    NORMALIZATION = "normalization"
    CLASSIFICATION = "classification"
    ENRICHMENT = "enrichment"
    SCORE = "score"
    PUBLICATION = "publication"

class PipelineJobSpec(BaseModel):
    step: ProcessingStep
    job_type: str
    depends_on: list[ProcessingStep] = []
    retryable: bool = True

PROCESSING_PIPELINE = [
    PipelineJobSpec(step=ProcessingStep.UPLOAD, job_type="upload"),
    PipelineJobSpec(step=ProcessingStep.VALIDATION, job_type="validation", depends_on=[ProcessingStep.UPLOAD]),
    PipelineJobSpec(step=ProcessingStep.EXTRACTION, job_type="extraction", depends_on=[ProcessingStep.VALIDATION]),
    PipelineJobSpec(step=ProcessingStep.NORMALIZATION, job_type="normalization", depends_on=[ProcessingStep.EXTRACTION]),
    PipelineJobSpec(step=ProcessingStep.CLASSIFICATION, job_type="classification", depends_on=[ProcessingStep.NORMALIZATION]),
    PipelineJobSpec(step=ProcessingStep.ENRICHMENT, job_type="enrichment", depends_on=[ProcessingStep.CLASSIFICATION]),
    PipelineJobSpec(step=ProcessingStep.SCORE, job_type="score", depends_on=[ProcessingStep.ENRICHMENT]),
    PipelineJobSpec(step=ProcessingStep.PUBLICATION, job_type="publication", depends_on=[ProcessingStep.SCORE]),
]
