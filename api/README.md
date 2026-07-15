# API

FastAPI backend for the Mini Telemetry Platform.

## Run locally

```powershell
cd api
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

Health endpoints:

- `GET /health/live`
- `GET /health/ready`

## Test

```powershell
cd api
python -m pytest
```

## Docker

```powershell
docker build -t mini-telemetry-api:dev api
docker run --rm --name mini-telemetry-api-dev -p 8001:8000 mini-telemetry-api:dev
```

Then open:

- `http://127.0.0.1:8001/health/live`
- `http://127.0.0.1:8001/health/ready`

## Compose with PostgreSQL

From the repository root:

```powershell
docker compose -f infra/compose/compose.yaml up -d db
cd api
$env:DATABASE_URL="postgresql+psycopg://telemetry:telemetry_dev_password@localhost:5433/telemetry"
..\.venv\Scripts\python.exe -m alembic upgrade head
```

For the full API + database stack, run from the repository root:

```powershell
docker compose -f infra/compose/compose.yaml up -d --build api
```
