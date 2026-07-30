from prometheus_client import Counter, Histogram


HTTP_REQUESTS = Counter(
    "http_requests_total",
    "Total HTTP requests handled by the API.",
    ("method", "route", "status"),
)

HTTP_REQUEST_DURATION = Histogram(
    "http_request_duration_seconds",
    "Time spent handling HTTP requests.",
    ("method", "route"),
)

MQTT_MESSAGES_RECEIVED = Counter(
    "mqtt_messages_received_total",
    "Total MQTT messages received by the API.",
)

MQTT_INVALID_PAYLOADS = Counter(
    "mqtt_invalid_payloads_total",
    "MQTT messages that could not be decoded or processed.",
)

TELEMETRY_INSERTED = Counter(
    "telemetry_inserted_total",
    "Telemetry readings inserted into PostgreSQL.",
)

TELEMETRY_DUPLICATES = Counter(
    "telemetry_duplicates_total",
    "Telemetry messages ignored because the message ID already exists.",
)

TELEMETRY_DATABASE_FAILURES = Counter(
    "telemetry_database_failures_total",
    "Telemetry messages that failed while writing to PostgreSQL.",
)
