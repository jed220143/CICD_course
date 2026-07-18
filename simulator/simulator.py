import json
import os
import random
import time
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

import paho.mqtt.client as mqtt

BROKER_HOST = os.getenv("MQTT_BROKER_HOST", "broker")
BROKER_PORT = int(os.getenv("MQTT_BROKER_PORT", "1883"))
TOPIC = os.getenv("MQTT_PUBLISH_TOPIC", "devices/sensor-001/telemetry")
DEVICE_KEY = os.getenv("DEVICE_KEY", "sensor-001")
INTERVAL_SECONDS = int(os.getenv("SIMULATOR_INTERVAL_SECONDS", "5"))
OUTPUT_DIR = Path(os.getenv("SIMULATOR_OUTPUT_DIR", "/app/out"))


def build_payload() -> dict[str, object]:
    return {
        "message_id": str(uuid4()),
        "device_key": DEVICE_KEY,
        "temperature_c": round(random.uniform(24.0, 34.0), 2),
        "humidity_percent": round(random.uniform(50.0, 80.0), 2),
        "recorded_at": datetime.now(timezone.utc).isoformat(),
    }


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id=f"{DEVICE_KEY}-simulator")
client.connect(BROKER_HOST, BROKER_PORT, keepalive=60)
client.loop_start()

while True:
    payload = build_payload()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / "latest-telemetry.json").write_text(
        json.dumps(payload, indent=2),
        encoding="utf-8",
    )
    with (OUTPUT_DIR / "telemetry.jsonl").open("a", encoding="utf-8") as file:
        file.write(json.dumps(payload) + "\n")

    client.publish(TOPIC, json.dumps(payload), qos=1)
    print(f"published {payload}", flush=True)
    time.sleep(INTERVAL_SECONDS)
