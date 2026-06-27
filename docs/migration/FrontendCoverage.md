# Frontend Coverage

## Estrutura analisada
- Rotas: 21
- Componentes: 53
- Services: 5
- Módulos declarados: 204

## Provider
`VITE_API_PROVIDER` seleciona `mock` ou `rest`; componentes importam a camada `services`.

## Fetch direto
Arquivos fora do HTTP client com `fetch(`: ['src/server.ts', 'src/integrations/supabase/auth-middleware.ts', 'src/integrations/supabase/client.ts', 'src/integrations/supabase/client.server.ts'].
