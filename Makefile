.PHONY: bootstrap lint format test seed reset build openapi sdk dev prod audit
bootstrap:
	python -m pip install -e 'backend[dev]'
lint:
	python -m compileall -q backend/app
format:
	python -m ruff format backend || true
test:
	PYTHONPATH=backend pytest backend/tests
seed:
	PYTHONPATH=backend python -c "from app.infrastructure.seeds.demo import build_demo_seed_summary; print(build_demo_seed_summary())"
reset:
	docker compose -f docker-compose.dev.yml down -v
build:
	docker compose -f docker-compose.dev.yml build
openapi:
	PYTHONPATH=backend python backend/scripts/generate_openapi.py
sdk: openapi
	PYTHONPATH=backend python backend/scripts/generate_sdk.py
audit: openapi sdk
	PYTHONPATH=backend python backend/scripts/audit_architecture.py
dev:
	docker compose -f docker-compose.dev.yml up --build
prod:
	docker compose -f docker-compose.prod.yml up --build -d
