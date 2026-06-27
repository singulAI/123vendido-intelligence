# Database

A fundação SQLAlchemy/Alembic cobre organizações, usuários, RBAC, billing, conectores, jobs, DLQ, organizadores, leilões, editais, lotes, veículos, análises versionadas, favoritos, relatórios, auditoria, Asset Center, Data Lake, versionamento, feature flags, Prompt Center, AI usage logs, cálculo financeiro, histórico e Knowledge Graph.

## Soft delete e UUID
Entidades principais usam UUID e `deleted_at` para soft delete.

## RBAC
Tabelas: `roles`, `permissions`, `permission_groups`, `role_permissions`, `user_roles`.

## Billing
Tabelas: `products`, `plans`, `trials`, `coupons`, `subscriptions`, `payments`, `invoices`, `pix_configurations`.

## Asset Center
Tabelas: `assets`, com documentos, imagens, anexos, thumbnails, metadata, hash, duplicidade, storage provider, OCR status e AI status.

## Data Lake
Tabela: `data_lake_entries`, com stages `raw_data`, `normalized_data`, `validated_data`, `enriched_data`, `ai_data` e `user_data`. O stage raw é imutável.

## Versionamento amplo
Tabela: `version_snapshots`, preparada para editais, lotes, veículos, imagens, configurações, conectores, planos, permissões e análises.

## Histórico completo
Tabela: `history_entries`, cobrindo análise, consulta, alteração, IA utilizada, prompt, score, decisão e cálculo.
