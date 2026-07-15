from fastapi import FastAPI

from app.config import get_settings
from app.logging import configure_logging

settings = get_settings()
configure_logging(settings)

app = FastAPI(title="Mini Telemetry API")


@app.get("/health/live")
def live() -> dict[str, str]:
    return {
        "status": "ok",
        "service": settings.service_name,
        "environment": settings.app_env,
    }


@app.get("/health/ready")
def ready() -> dict[str, str]:
    return {
        "status": "ready",
        "service": settings.service_name,
    }
