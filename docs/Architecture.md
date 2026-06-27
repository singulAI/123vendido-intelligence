# 123Vendido Backend Architecture

Backend enterprise em Python 3.13+ com FastAPI, SQLAlchemy Async, Alembic, PostgreSQL, Redis, JWT, Loguru-ready, Prometheus em `/metrics` e OpenTelemetry-ready.

## Camadas
- **Core**: configuração, segurança e cross-cutting concerns.
- **Domain**: entidades, contratos e políticas desacopladas.
- **Application**: orquestração de casos de uso.
- **Infrastructure**: banco, repositórios, storage, jobs, event bus e providers mock.
- **Interfaces/API**: API HTTP versionada em `/api/v1`.
- **AI / Vision / Knowledge / Jobs / Connectors / Storage / Billing / Monitoring / Developer Center / Audit / Notifications / Security / Reports**: módulos evolutivos isolados.

## Princípios
- API não integrada ao frontend nesta fase.
- Autorização dinâmica por permissões, nunca por perfil fixo.
- Análises e dados operacionais versionados, sem sobrescrever resultados.
- IA e visão computacional apenas por contratos e mocks.
- Contexto enriquecido obrigatório para análise de lote.
- Dados originais do Data Lake são imutáveis.

## Intelligence Pipelines independentes
- Market Intelligence
- Opportunity Engine
- Risk Engine
- Repair Cost Engine
- Liquidity Engine
- Pricing Engine
- Recommendation Engine
- Vision Engine
- Document Intelligence
- AI Orchestrator
- Knowledge Graph

## Pipeline de processamento
Upload → Validation → Extraction → Normalization → Classification → Enrichment → Score → Publication. Cada etapa é modelada como Job independente, com dependência e retry próprios.

## Fase Final de Consolidação
- **Decision Engine** consolida engines independentes em uma recomendação única.
- **Score 360°** padroniza Opportunity, Risk, Repair, Market, Liquidity, ROI, Confidence e Final Auction Score.
- **Timeline Inteligente** registra eventos relevantes por lote para análise histórica.
- **Radar Inteligente** prepara watchlists, saved searches e alertas.
- **Data Warehouse** separa base operacional, Data Lake, Warehouse, Analytics e Dashboard.
- **API Gateway Contracts** preparam auth, rate limit, cache, REST, futuro GraphQL e futuro WebSocket.
- **AI Context Builder** garante que nenhuma IA receba somente imagens; contexto inclui veículo, edital, lote, organizador, observações, histórico, mercado e imagens.
- **Semantic Search** prepara embeddings, vector database, semantic search, context retrieval e LLM.
- **AI Memory** registra prompt, resposta, feedback, correção, aprendizado e histórico.
- **Plugin System** organiza conectores, AI providers, billing, maps, storage, identity e government APIs.
- **Repository, Unit of Work, Specification, Query Objects, Redis Cache e Scheduler** consolidam padrões para consumo futuro pelo frontend.
