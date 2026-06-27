# Dependency Graph

FastAPI → API Router → Domain Contracts → Application Patterns → Infrastructure Adapters.

PostgreSQL é acessado por SQLAlchemy Async; Redis é acessado pelo cache distribuído; OpenAPI alimenta o SDK TypeScript; Docker Compose orquestra API, PostgreSQL e Redis.
