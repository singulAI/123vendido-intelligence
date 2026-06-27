/* Auto-generated from backend/openapi.json. Do not edit manually. */
export type ApiResponse<T = unknown> = { success: boolean; data: T; meta: Record<string, unknown>; errors: Array<Record<string, unknown>> };
export type HttpMethod = 'GET' | 'POST' | 'PUT' | 'PATCH' | 'DELETE';
export type EndpointSpec = { method: HttpMethod; path: string; operationId: string };
export const endpoints = [
  { method: 'GET' as const, path: '/api/v1/architecture/decisioning', operationId: 'decisioning_api_v1_architecture_decisioning_get' },
  { method: 'GET' as const, path: '/api/v1/architecture/growth-modules', operationId: 'growth_modules_api_v1_architecture_growth_modules_get' },
  { method: 'GET' as const, path: '/api/v1/architecture/pipelines', operationId: 'architecture_pipelines_api_v1_architecture_pipelines_get' },
  { method: 'GET' as const, path: '/api/v1/architecture/platform-controls', operationId: 'platform_controls_api_v1_architecture_platform_controls_get' },
  { method: 'GET' as const, path: '/api/v1/connectors', operationId: 'connectors_api_v1_connectors_get' },
  { method: 'GET' as const, path: '/api/v1/connectors/{provider}/health', operationId: 'connector_health_api_v1_connectors__provider__health_get' },
  { method: 'GET' as const, path: '/api/v1/health', operationId: 'health_api_v1_health_get' },
  { method: 'POST' as const, path: '/api/v1/intelligence/mock-analysis', operationId: 'mock_analysis_api_v1_intelligence_mock_analysis_post' },
  { method: 'GET' as const, path: '/api/v1/modules', operationId: 'modules_api_v1_modules_get' },
] as const;
export type Endpoint = typeof endpoints[number];
export class VendidoApiClient { constructor(private baseUrl: string, private token?: string) {} async request<T>(endpoint: Endpoint, init: RequestInit = {}): Promise<ApiResponse<T>> { const response = await fetch(`${this.baseUrl}${endpoint.path}`, { ...init, method: endpoint.method, headers: { 'Content-Type': 'application/json', ...(this.token ? { Authorization: `Bearer ${this.token}` } : {}), ...(init.headers || {}) } }); return response.json(); } }
