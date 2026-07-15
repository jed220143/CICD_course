import json
import logging
import threading

import paho.mqtt.client as mqtt

from app.config import get_settings
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
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="mini-telemetry-api")

    def on_connect(client: mqtt.Client, userdata, flags, reason_code, properties) -> None:
        logger.info("Connected to MQTT broker: %s", reason_code)
        client.subscribe(settings.mqtt_topic)

    def on_message(client: mqtt.Client, userdata, message: mqtt.MQTTMessage) -> None:
        try:
            payload = json.loads(message.payload.decode("utf-8"))
            inserted = store_telemetry(payload)
            logger.info("Telemetry message processed: inserted=%s topic=%s", inserted, message.topic)
        except Exception:
            logger.exception("Failed to process telemetry message from topic=%s", message.topic)

    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(settings.mqtt_broker_host, settings.mqtt_broker_port, keepalive=60)
    client.loop_forever()
