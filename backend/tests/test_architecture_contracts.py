from app.domain.ai.contracts import AIProvider
from app.domain.data_lake.contracts import DataLakeStage, IMMUTABLE_STAGES
from app.domain.feature_flags.contracts import FeatureKey
from app.domain.intelligence.pipelines import PIPELINE_ORDER, IntelligencePipeline
from app.domain.pipelines.contracts import PROCESSING_PIPELINE, ProcessingStep
from app.domain.finance.contracts import FinancialInputs, calculate_financial_result


def test_independent_intelligence_pipelines_are_declared():
    assert IntelligencePipeline.MARKET in PIPELINE_ORDER
    assert IntelligencePipeline.VISION in PIPELINE_ORDER
    assert IntelligencePipeline.KNOWLEDGE_GRAPH in PIPELINE_ORDER


def test_processing_pipeline_promotes_upload_to_publication_jobs():
    assert [job.step for job in PROCESSING_PIPELINE] == [
        ProcessingStep.UPLOAD,
        ProcessingStep.VALIDATION,
        ProcessingStep.EXTRACTION,
        ProcessingStep.NORMALIZATION,
        ProcessingStep.CLASSIFICATION,
        ProcessingStep.ENRICHMENT,
        ProcessingStep.SCORE,
        ProcessingStep.PUBLICATION,
    ]


def test_data_lake_preserves_raw_stage():
    assert DataLakeStage.RAW in IMMUTABLE_STAGES
    assert DataLakeStage.AI.value == "ai_data"
    assert DataLakeStage.USER.value == "user_data"


def test_feature_flags_and_multi_ai_are_explicit():
    assert FeatureKey.OLLAMA.value == "ollama"
    assert FeatureKey.BILLING.value == "billing"
    assert AIProvider.OPENAI.value == "openai"
    assert AIProvider.CUSTOM.value == "custom_models"


def test_financial_engine_calculates_roi_score():
    result = calculate_financial_result(FinancialInputs(notice_value_cents=50000, market_price_cents=80000, estimated_cost_cents=10000))
    assert result.profit_cents == 20000
    assert result.roi_percent > 0
    assert result.score > 50
