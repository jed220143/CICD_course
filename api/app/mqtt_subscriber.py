import json
import logging
import threading
import time

import paho.mqtt.client as mqtt

from app.config import get_settings
from app.metrics import (
    MQTT_INVALID_PAYLOADS,
    MQTT_MESSAGES_RECEIVED,
    TELEMETRY_DATABASE_FAILURES,
    TELEMETRY_DUPLICATES,
    TELEMETRY_INSERTED,
)
from app.telemetry import store_telemetry

logger = logging.getLogger(__name__)
_started = False


def start_subscriber() -> None:
    global _started
    settings = get_settings()

    if _started or not settings.mqtt_broker_host:
        return

    _started = True
    thread = threading.Thread(target=_run_subscriber, daemon=True)
    thread.start()


def _run_subscriber() -> None:
    settings = get_settings()

    def on_connect(client: mqtt.Client, userdata, flags, reason_code, properties) -> None:
        logger.info("Connected to MQTT broker: %s", reason_code)
        client.subscribe(settings.mqtt_topic)

    def on_message(client: mqtt.Client, userdata, message: mqtt.MQTTMessage) -> None:
        MQTT_MESSAGES_RECEIVED.inc()

        try:
            payload = json.loads(message.payload.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            MQTT_INVALID_PAYLOADS.inc()
            logger.exception("Invalid MQTT payload from topic=%s", message.topic)
            return

        try:
            inserted = store_telemetry(payload)
            if inserted:
                TELEMETRY_INSERTED.inc()
            else:
                TELEMETRY_DUPLICATES.inc()
            logger.info("Telemetry message processed: inserted=%s topic=%s", inserted, message.topic)
        except Exception:
            TELEMETRY_DATABASE_FAILURES.inc()
            logger.exception("Failed to process telemetry message from topic=%s", message.topic)

    while True:
        try:
            client = mqtt.Client(
                mqtt.CallbackAPIVersion.VERSION2,
                client_id="mini-telemetry-api",
            )
            client.on_connect = on_connect
            client.on_message = on_message
            client.connect(settings.mqtt_broker_host, settings.mqtt_broker_port, keepalive=60)
            client.loop_forever()
            logger.warning("MQTT loop stopped; reconnecting in 5 seconds")
        except Exception:
            logger.exception("MQTT subscriber failed; reconnecting in 5 seconds")

        time.sleep(5)
