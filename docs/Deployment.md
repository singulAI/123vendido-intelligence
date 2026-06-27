# Deployment

Infra alvo: VPS com Docker, Docker Compose, PostgreSQL, Redis, Nginx, n8n, Ollama/Mistral e GitHub Actions.

## Local
```bash
docker compose -f docker-compose.backend.yml up --build
```

## Produção
- Configurar secrets `VENDIDO_*`.
- Executar Alembic antes de subir novas versões.
- Publicar API atrás do Nginx com TLS.
- Manter n8n/Ollama como serviços internos acessíveis por conectores futuros.
