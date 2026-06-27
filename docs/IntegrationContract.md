# Integration Contract

Este documento congela os contratos backend antes de qualquer integração com o frontend Lovable. O frontend poderá substituir Mock Providers por chamadas reais sem alterações estruturais de UX.

## Envelope padrão
Todas as respostas HTTP seguem:
```json
{"success": true, "data": {}, "meta": {}, "errors": []}
```

## Endpoints atuais
- `GET /api/v1/health`: status da API.
- `GET /api/v1/connectors`: providers suportados.
- `GET /api/v1/connectors/{provider}/health`: health check mock do provider.
- `POST /api/v1/intelligence/mock-analysis`: executa engines mock sobre `LotAnalysisContext`.
- `GET /api/v1/modules`: módulos implementados e pendentes.
- `GET /api/v1/architecture/pipelines`: intelligence pipelines, processing pipeline e Data Lake stages.
- `GET /api/v1/architecture/platform-controls`: feature flags e AI providers.
- `GET /api/v1/architecture/decisioning`: exemplo de Score 360 e Decision Engine.
- `GET /api/v1/architecture/growth-modules`: timeline, radar alerts e plugin kinds.

## DTOs principais
- `LotAnalysisContext`: edital, lote, veículo, imagens, URL oficial, observações, informações conhecidas, histórico e fontes.
- `Score360`: opportunity, risk, repair, market, liquidity, ROI, confidence e final auction score.
- `DecisionResult`: score final consolidado, recomendação, racional, confiança e limitações.
- `AssetMetadata`: documentos, imagens, anexos, thumbnails, hash, duplicidade, storage, OCR e AI status.
- `DataLakeRecord`: Raw, Normalized, Validated, Enriched, AI e User Data.
- `PipelineJobSpec`: etapa de processamento, tipo de job, dependências e retry.
- `FeatureFlag`: chave, estado, rollout e regras.
- `AIRequest`: prompt template, variáveis e política de seleção/fallback/custo/rate limit.
- `PromptTemplate`: chave, versão, provider, variáveis, temperature, max tokens e fallback.
- `FinancialInputs`/`FinancialResult`: entradas financeiras e resultado ROI/score.

## OpenAPI
Gerar especificação localmente:
```bash
PYTHONPATH=backend python backend/scripts/generate_openapi.py
```
