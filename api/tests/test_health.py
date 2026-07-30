from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_live_health() -> None:
    response = client.get("/health/live")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_ready_health() -> None:
    response = client.get("/health/ready")

    assert response.status_code == 200
    assert response.json()["status"] == "ready"


def test_metrics_endpoint_exposes_application_metrics() -> None:
    client.get("/health/live")

    response = client.get("/metrics")

    assert response.status_code == 200
    assert "http_requests_total" in response.text
    assert "mqtt_messages_received_total" in response.text


def test_response_contains_request_id() -> None:
    response = client.get("/health/live")

    assert response.headers["X-Request-ID"]


def test_valid_incoming_request_id_is_preserved() -> None:
    response = client.get(
        "/health/live",
        headers={"X-Request-ID": "learning-request-001"},
    )

    assert response.headers["X-Request-ID"] == "learning-request-001"
