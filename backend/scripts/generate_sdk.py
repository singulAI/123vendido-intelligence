import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
openapi = json.loads((ROOT / "backend/openapi.json").read_text())
out = ROOT / "backend/client-sdk-typescript/src/index.ts"

def pascal(value: str) -> str:
    return "".join(part.capitalize() for part in re.split(r"[^a-zA-Z0-9]+", value) if part)

lines = ["/* Auto-generated from backend/openapi.json. Do not edit manually. */", "export type ApiResponse<T = unknown> = { success: boolean; data: T; meta: Record<string, unknown>; errors: Array<Record<string, unknown>> };", "export type HttpMethod = 'GET' | 'POST' | 'PUT' | 'PATCH' | 'DELETE';", "export type EndpointSpec = { method: HttpMethod; path: string; operationId: string };", "export const endpoints = ["]
for path, methods in sorted(openapi.get("paths", {}).items()):
    for method, operation in sorted(methods.items()):
        lines.append(f"  {{ method: '{method.upper()}' as const, path: '{path}', operationId: '{operation.get('operationId', pascal(method + '_' + path))}' }},")
lines.append("] as const;")
lines.append("export type Endpoint = typeof endpoints[number];")
lines.append("export class VendidoApiClient { constructor(private baseUrl: string, private token?: string) {} async request<T>(endpoint: Endpoint, init: RequestInit = {}): Promise<ApiResponse<T>> { const response = await fetch(`${this.baseUrl}${endpoint.path}`, { ...init, method: endpoint.method, headers: { 'Content-Type': 'application/json', ...(this.token ? { Authorization: `Bearer ${this.token}` } : {}), ...(init.headers || {}) } }); return response.json(); } }")
out.write_text("\n".join(lines) + "\n")
print(out)
