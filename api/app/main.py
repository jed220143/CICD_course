from contextlib import asynccontextmanager
from collections.abc import AsyncIterator
import logging
import re
from time import perf_counter
from uuid import uuid4

from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest

from app.config import get_settings
from app.db import check_database
from app.logging import configure_logging
from app.metrics import HTTP_REQUEST_DURATION, HTTP_REQUESTS
from app.mqtt_subscriber import start_subscriber
from app.read_api import router as read_router

settings = get_settings()
configure_logging(settings)
logger = logging.getLogger(__name__)
REQUEST_ID_PATTERN = re.compile(r"^[A-Za-z0-9._-]{1,128}$")


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    start_subscriber()
    yield


app = FastAPI(title="Mini Telemetry API", lifespan=lifespan)
app.include_router(read_router)


@app.middleware("http")
async def observe_http_request(request: Request, call_next):
    started_at = perf_counter()
    status_code = 500
    incoming_request_id = request.headers.get("X-Request-ID", "")
    request_id = (
        incoming_request_id
        if REQUEST_ID_PATTERN.fullmatch(incoming_request_id)
        else str(uuid4())
    )

    try:
        response = await call_next(request)
        status_code = response.status_code
        response.headers["X-Request-ID"] = request_id
        return response
    finally:
        route = request.scope.get("route")
        route_path = getattr(route, "path", "unmatched")
        duration_seconds = perf_counter() - started_at
        HTTP_REQUESTS.labels(
            method=request.method,
            route=route_path,
            status=str(status_code),
        ).inc()
        HTTP_REQUEST_DURATION.labels(
            method=request.method,
            route=route_path,
        ).observe(duration_seconds)
        logger.info(
            "http_request request_id=%s method=%s route=%s status=%s duration_ms=%.2f",
            request_id,
            request.method,
            route_path,
            status_code,
            duration_seconds * 1000,
        )


@app.get("/metrics", include_in_schema=False)
def metrics() -> Response:
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)


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
