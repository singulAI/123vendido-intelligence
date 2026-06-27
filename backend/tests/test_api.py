from fastapi.testclient import TestClient
from app.main import app

def test_health_response_shape():
    response = TestClient(app).get("/api/v1/health")
    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True
    assert body["data"]["status"] == "ok"
    assert body["errors"] == []

def test_connectors_are_mocked():
    response = TestClient(app).get("/api/v1/connectors/ollama/health")
    assert response.status_code == 200
    assert response.json()["data"]["healthy"] is True
