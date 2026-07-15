from datetime import datetime
from typing import Any

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from app.db import create_session
from app.models import Device, TelemetryReading


def store_telemetry(payload: dict[str, Any]) -> bool:
    message_id = str(payload["message_id"])
    device_key = str(payload["device_key"])
    recorded_at = datetime.fromisoformat(str(payload["recorded_at"]).replace("Z", "+00:00"))

    with create_session() as session:
        device = session.scalar(select(Device).where(Device.device_key == device_key))
        if device is None:
            device = Device(device_key=device_key, name=device_key)
            session.add(device)
            session.flush()

        reading = TelemetryReading(
            message_id=message_id,
            device_id=device.id,
            temperature_c=payload.get("temperature_c"),
            humidity_percent=payload.get("humidity_percent"),
            recorded_at=recorded_at.replace(tzinfo=None),
        )
        session.add(reading)

        try:
            session.commit()
        except IntegrityError:
            session.rollback()
            return False

    return True
