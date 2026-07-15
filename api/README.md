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
