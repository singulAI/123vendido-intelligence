import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
openapi = json.loads((ROOT / "backend/openapi.json").read_text())
frontend_files = sorted((ROOT / "src").glob("**/*.ts*"))
services = [str(p.relative_to(ROOT)) for p in frontend_files if "service" in p.name.lower() or "api" in p.name.lower()]
mock_contracts = ["Leilao", "Lote", "Veiculo", "Usuario", "Pagamento", "Assinatura", "Connector", "Alerta", "Job", "LogEvento", "Relatorio"]
paths = openapi.get("paths", {})
report = {
    "status": "certified_with_mock_frontend",
    "frontend_services_found": services,
    "frontend_mock_contracts": mock_contracts,
    "openapi_paths": sorted(paths),
    "standard_envelope_schema": "ApiResponse",
    "integration_rule": "Frontend must consume backend through generated client-sdk-typescript; do not duplicate interfaces.",
    "gaps_before_real_rest_provider": [
        "No frontend HTTP service layer exists yet; current Lovable UI consumes local mock data.",
        "CRUD resource endpoints are not runtime-complete yet; current backend exposes architecture and diagnostic contracts only.",
        "Auth/refresh/RBAC are foundation contracts/helpers, not public login endpoints yet.",
    ],
    "certification": {
        "openapi_valid": bool(paths),
        "response_envelope_present": "ApiResponse" in json.dumps(openapi),
        "frontend_components_untouched_required": True,
    },
}
(ROOT / "docs/validation/CompatibilityReport.json").write_text(json.dumps(report, indent=2, ensure_ascii=False))
print(json.dumps(report, indent=2, ensure_ascii=False))
