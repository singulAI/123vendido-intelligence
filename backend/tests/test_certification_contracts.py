import json
from pathlib import Path

from fastapi.testclient import TestClient
from jose import jwt

from app.core.config import get_settings
from app.core.security import create_token
from app.domain.feature_flags.contracts import FeatureFlag, FeatureKey
from app.domain.jobs import __name__ as jobs_domain_name
from app.domain.score.contracts import Score360
from app.main import app

ROOT = Path(__file__).resolve().parents[2]


def test_openapi_json_schema_and_standard_response_envelope_are_present():
    schema = json.loads((ROOT / "backend/openapi.json").read_text())
    assert schema["openapi"].startswith("3.")
    assert "ApiResponse" in schema["components"]["schemas"]
    assert set(schema["components"]["schemas"]["ApiResponse"]["properties"]) >= {"success", "data", "meta", "errors"}


def test_all_runtime_endpoints_return_standard_envelope_for_success():
    client = TestClient(app)
    for path in [
        "/api/v1/health",
        "/api/v1/connectors",
        "/api/v1/connectors/ollama/health",
        "/api/v1/modules",
        "/api/v1/architecture/pipelines",
        "/api/v1/architecture/platform-controls",
        "/api/v1/architecture/decisioning",
        "/api/v1/architecture/growth-modules",
    ]:
        body = client.get(path).json()
        assert set(body) == {"success", "data", "meta", "errors"}
        assert body["success"] is True
        assert body["errors"] == []


def test_jwt_access_token_contract_contains_subject_type_and_expiry():
    token = create_token("user-123")
    payload = jwt.decode(token, get_settings().jwt_secret_key, algorithms=[get_settings().jwt_algorithm])
    assert payload["sub"] == "user-123"
    assert payload["type"] == "access"
    assert "exp" in payload


def test_feature_flags_permissions_and_jobs_contracts_are_importable():
    flag = FeatureFlag(key=FeatureKey.OCR, enabled=False)
    assert flag.key == FeatureKey.OCR
    assert jobs_domain_name == "app.domain.jobs"


def test_sdk_was_generated_from_openapi_paths():
    sdk = (ROOT / "backend/client-sdk-typescript/src/index.ts").read_text()
    assert "Auto-generated from backend/openapi.json" in sdk
    assert "/api/v1/health" in sdk
    assert "VendidoApiClient" in sdk


def test_score_360_schema_validates_boundaries():
    score = Score360.weighted(opportunity_score=100, risk_score=0, repair_score=100, market_score=100, liquidity_score=100, roi_score=100, confidence_score=100)
    assert 0 <= score.final_auction_score <= 100
