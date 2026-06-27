# Migration Report

## Fonte
Frontend definitivo clonado de `https://github.com/singulAI/um23vendidoem.git`.

## Resultado
O frontend legado da raiz foi removido e o frontend oficial foi instalado em `/frontend`, preservando `/backend`, `/docs`, `/scripts`, `/.github`, Docker/Compose, OpenAPI, SDK e infraestrutura.

## Ajustes não visuais
- Corrigida string de metadata com quebra de linha inválida em `frontend/src/routes/__root.tsx` para permitir build.
- `frontend/src/lib/api/http-client.ts` agora reconhece e desembrulha o envelope `ApiResponse` do backend, mantendo componentes desacoplados de endpoints.

## Segurança
O arquivo `.env` clonado não foi migrado para evitar versionamento de credenciais; permanece apenas `.env.example`.
