from app.domain.connectors.contracts import ConnectorConfig, ConnectorHealth

class MockConnectorProvider:
    def __init__(self, provider: str):
        self.config = ConnectorConfig(provider=provider)
    async def health_check(self) -> ConnectorHealth:
        return ConnectorHealth(provider=self.config.provider, healthy=True, details={"mode": "mock"})

SUPPORTED_PROVIDERS = ["fipe", "brasilapi", "receita_federal", "serpro", "detrans", "google_maps", "openstreetmap", "mercado_livre", "olx", "webmotors", "openai", "ollama", "fastapi", "n8n"]
