from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_client import make_asgi_app
from app.core.config import get_settings
from app.interfaces.api.v1.router import router as v1_router

settings = get_settings()
app = FastAPI(title=settings.app_name, version="0.1.0", openapi_url=f"{settings.api_prefix}/openapi.json")
app.add_middleware(CORSMiddleware, allow_origins=settings.cors_origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.include_router(v1_router, prefix=settings.api_prefix)
app.mount("/metrics", make_asgi_app())
