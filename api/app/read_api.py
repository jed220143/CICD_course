from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import desc, func, select
from sqlalchemy.orm import Session

from app.db import get_session
from app.models import Device, TelemetryReading

router = APIRouter()
SessionDep = Annotated[Session, Depends(get_session)]


@router.get("/devices")
def list_devices(session: SessionDep) -> list[dict[str, object]]:
    rows = session.execute(
        select(Device, func.count(TelemetryReading.id))
        .outerjoin(TelemetryReading)
        .group_by(Device.id)
        .order_by(Device.device_key)
    ).all()

    return [
        {
            "device_key": device.device_key,
            "name": device.name,
            "reading_count": reading_count,
            "created_at": device.created_at,
        }
        for device, reading_count in rows
    ]


@router.get("/devices/{device_key}/readings")
def list_device_readings(
    device_key: str,
    session: SessionDep,
    limit: Annotated[int, Query(ge=1, le=100)] = 20,
) -> list[dict[str, object]]:
    device = session.scalar(select(Device).where(Device.device_key == device_key))
    if device is None:
        raise HTTPException(status_code=404, detail="Device not found")

    readings = session.scalars(
        select(TelemetryReading)
        .where(TelemetryReading.device_id == device.id)
        .order_by(desc(TelemetryReading.recorded_at))
        .limit(limit)
    ).all()

    return [_reading_to_dict(device, reading) for reading in readings]


@router.get("/telemetry/latest")
def latest_telemetry(
    session: SessionDep,
    limit: Annotated[int, Query(ge=1, le=100)] = 20,
) -> list[dict[str, object]]:
    rows = session.execute(
        select(Device, TelemetryReading)
        .join(TelemetryReading)
        .order_by(desc(TelemetryReading.recorded_at))
        .limit(limit)
    ).all()

    return [_reading_to_dict(device, reading) for device, reading in rows]


def _reading_to_dict(device: Device, reading: TelemetryReading) -> dict[str, object]:
    return {
        "message_id": reading.message_id,
        "device_key": device.device_key,
        "temperature_c": reading.temperature_c,
        "humidity_percent": reading.humidity_percent,
        "recorded_at": reading.recorded_at,
    }
