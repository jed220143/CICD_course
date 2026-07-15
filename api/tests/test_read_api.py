from collections.abc import Generator
from datetime import datetime

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool

from app.db import Base, get_session
from app.main import app
from app.models import Device, TelemetryReading


def build_client() -> TestClient:
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(engine)
    session_factory = sessionmaker(bind=engine)

    with session_factory() as session:
        device = Device(device_key="sensor-001", name="sensor-001")
        session.add(device)
        session.flush()
        session.add(
            TelemetryReading(
                message_id="test-message-001",
                device_id=device.id,
                temperature_c=29.5,
                humidity_percent=61.0,
                recorded_at=datetime(2026, 7, 15, 12, 0, 0),
            )
        )
        session.commit()

    def override_session() -> Generator[Session, None, None]:
        with session_factory() as session:
            yield session

    app.dependency_overrides[get_session] = override_session
    return TestClient(app)


def test_list_devices() -> None:
    client = build_client()

    response = client.get("/devices")

    assert response.status_code == 200
    assert response.json()[0]["device_key"] == "sensor-001"
    assert response.json()[0]["reading_count"] == 1

    app.dependency_overrides.clear()


def test_latest_telemetry() -> None:
    client = build_client()

    response = client.get("/telemetry/latest")

    assert response.status_code == 200
    assert response.json()[0]["message_id"] == "test-message-001"
    assert response.json()[0]["temperature_c"] == 29.5

    app.dependency_overrides.clear()
