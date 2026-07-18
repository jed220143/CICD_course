from contextlib import asynccontextmanager
from collections.abc import AsyncIterator

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.config import get_settings
from app.db import check_database
from app.logging import configure_logging
from app.mqtt_subscriber import start_subscriber
from app.read_api import router as read_router

settings = get_settings()
configure_logging(settings)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    start_subscriber()
    yield


app = FastAPI(title="Mini Telemetry API", lifespan=lifespan)
app.include_router(read_router)


@app.get("/health/live")
def live() -> dict[str, str]:
    return {
        "status": "ok",
        "service": settings.service_name,
        "environment": settings.app_env,
    }


@app.get("/health/ready", response_model=None)
def ready() -> dict[str, str] | JSONResponse:
    if settings.database_url:
        try:
            check_database()
        except Exception:
            return JSONResponse(
                status_code=503,
                content={
                    "status": "not_ready",
                    "service": settings.service_name,
                    "database": "unavailable",
                },
            )

    return {
        "status": "ready",
        "service": settings.service_name,
        "database": "ok" if settings.database_url else "not_configured",
    }
