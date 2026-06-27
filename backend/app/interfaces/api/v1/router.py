from fastapi import APIRouter
from app.infrastructure.connectors.mock import SUPPORTED_PROVIDERS, MockConnectorProvider
from app.infrastructure.connectors.intelligence_mock import ENGINE_NAMES, MockIntelligenceEngine
from app.domain.intelligence.contracts import LotAnalysisContext
from app.interfaces.api.v1.schemas import ApiResponse
from app.domain.intelligence.pipelines import PIPELINE_ORDER
from app.domain.pipelines.contracts import PROCESSING_PIPELINE
from app.domain.feature_flags.contracts import FeatureKey
from app.domain.ai.contracts import AIProvider
from app.domain.data_lake.contracts import DataLakeStage
from app.domain.score.contracts import Score360
from app.domain.decision.contracts import DecisionEngine, DecisionInput
from app.domain.timeline.contracts import TimelineEventType
from app.domain.radar.contracts import AlertKind
from app.domain.plugins.contracts import PluginKind

router = APIRouter()

@router.get("/health", response_model=ApiResponse)
async def health() -> ApiResponse:
    return ApiResponse(data={"status": "ok", "service": "123vendido-backend"})

@router.get("/connectors", response_model=ApiResponse)
async def connectors() -> ApiResponse:
    return ApiResponse(data={"providers": SUPPORTED_PROVIDERS})

@router.get("/connectors/{provider}/health", response_model=ApiResponse)
async def connector_health(provider: str) -> ApiResponse:
    health_result = await MockConnectorProvider(provider).health_check()
    return ApiResponse(data=health_result.model_dump())

@router.post("/intelligence/mock-analysis", response_model=ApiResponse)
async def mock_analysis(context: LotAnalysisContext) -> ApiResponse:
    results = [await MockIntelligenceEngine(name).analyze(context) for name in ENGINE_NAMES]
    return ApiResponse(data={"versioned": True, "results": [result.model_dump() for result in results]})

@router.get("/modules", response_model=ApiResponse)
async def modules() -> ApiResponse:
    implemented = ["auth-foundation", "users", "organizations", "rbac", "billing", "connectors-contracts", "jobs-foundation", "asset-center", "data-lake", "processing-pipeline", "versioning", "feature-flags", "multi-ai-contracts", "prompt-center", "financial-engine", "history", "uploads-storage-contracts", "auctions", "lots", "vehicles", "favorites", "reports", "audit", "monitoring", "intelligence-pipelines", "vision-contracts", "event-bus", "decision-engine", "score-360", "timeline", "radar", "data-warehouse", "api-gateway-contracts", "ai-context-builder", "semantic-search", "ai-memory", "plugin-system", "repository-pattern", "unit-of-work", "specifications", "query-objects", "redis-cache", "scheduler"]
    pending = ["parser-runtime", "ocr-runtime", "ai-runtime", "computer-vision-runtime", "crawlers", "external-provider-integrations", "frontend-integration"]
    return ApiResponse(data={"implemented": implemented, "pending": pending})


@router.get("/architecture/pipelines", response_model=ApiResponse)
async def architecture_pipelines() -> ApiResponse:
    return ApiResponse(data={
        "intelligence_pipelines": [pipeline.value for pipeline in PIPELINE_ORDER],
        "processing_pipeline": [job.model_dump() for job in PROCESSING_PIPELINE],
        "data_lake_stages": [stage.value for stage in DataLakeStage],
    })

@router.get("/architecture/platform-controls", response_model=ApiResponse)
async def platform_controls() -> ApiResponse:
    return ApiResponse(data={
        "feature_flags": [feature.value for feature in FeatureKey],
        "ai_providers": [provider.value for provider in AIProvider],
    })


@router.get("/architecture/decisioning", response_model=ApiResponse)
async def decisioning() -> ApiResponse:
    score = Score360.weighted(opportunity_score=80, risk_score=30, repair_score=70, market_score=75, liquidity_score=65, roi_score=85, confidence_score=75)
    decision = DecisionEngine().decide(DecisionInput(lot_id="demo", score_360=score))
    return ApiResponse(data={"score_360": score.model_dump(), "decision": decision.model_dump()})

@router.get("/architecture/growth-modules", response_model=ApiResponse)
async def growth_modules() -> ApiResponse:
    return ApiResponse(data={
        "timeline_events": [event.value for event in TimelineEventType],
        "radar_alerts": [alert.value for alert in AlertKind],
        "plugin_kinds": [plugin.value for plugin in PluginKind],
    })
