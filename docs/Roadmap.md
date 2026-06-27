# Roadmap

## Implementado
- Fundação FastAPI versionada.
- Modelos e migration inicial.
- RBAC dinâmico.
- Billing expansível.
- Asset Center para documentos, imagens, anexos, thumbnails, metadata, hash, duplicidade e status OCR/AI.
- Data Lake com Raw, Normalized, Validated, Enriched, AI e User Data sem alterar o original.
- Pipeline de processamento por Jobs: Upload, Validation, Extraction, Normalization, Classification, Enrichment, Score e Publication.
- Versionamento amplo para editais, lotes, veículos, imagens, configurações, conectores, planos, permissões e análises.
- Feature Flags para Vision AI, OCR, Parser, Radar, Marketplace, Crawler, Scrapers, OpenAI, Ollama, Mistral, Billing e Developer Center.
- Multi IA com AI Provider Manager conceitual, Prompt Router, Model Selector, Fallback, Cost Control e Rate Limit.
- Prompt Center com templates, versões, variáveis, testes, provider, temperature, max tokens e fallback.
- Motor financeiro separado para preço FIPE, preço mercado, valor edital, custos, impostos, frete, comissão, documentação, margem, lucro, ROI, payback e score.
- Histórico completo para análises, consultas, alterações, IA, prompts, scores, decisões e cálculos.
- Connectors com contratos e health mock.
- Jobs e DLQ em modelo de dados.
- Event bus em memória.
- Intelligence pipelines independentes.
- Vision Intelligence contracts.
- Documentação operacional inicial.

## Pendente
- CRUDs completos por domínio.
- OAuth Google runtime.
- Rate limit persistente.
- Workers Redis reais.
- Storage provider real.
- Parsers, OCR, IA e visão computacional reais.
- Integrações FIPE/BrasilAPI/SERPRO/Detrans/marketplaces.
- Relatório de integração frontend após entrega oficial.

## Consolidação final adicionada
- Decision Engine e Score 360°.
- Timeline Inteligente por lote.
- Radar Inteligente com watchlists, saved searches e alertas.
- Data Warehouse e Analytics separados da base operacional.
- API Gateway contracts para auth, rate limit, cache, REST, GraphQL futuro e WebSocket futuro.
- AI Context Builder, Semantic Search e AI Memory.
- Plugin System acima de connectors/providers.
- Repository genérico, Unit of Work, Specification Pattern, Query Objects, Redis Cache e Scheduler.
- Plano de seeds em escala e geração local de OpenAPI.
