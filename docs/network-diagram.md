# Network Diagram

```text
Host browser
  | HTTP localhost:8080
  v
nginx service
  | HTTP inside Docker network: api:8000
  v
api service
  | HTTP inside container: 0.0.0.0:8000
  | PostgreSQL connection: db:5432
  | MQTT subscribe: broker:1883 / devices/+/telemetry
  v
db service
  | stores data at /var/lib/postgresql/data
  v
Docker named volume: compose_postgres_data

simulator service
  | MQTT publish: devices/sensor-001/telemetry
  v
broker service
  | forwards messages to subscribers
  v
api service
```

## Ports

| Service | Container port | Host port | Purpose |
|---|---:|---:|---|
| nginx | 80 | 8080 | เส้นทางเข้าใช้งานหลัก |
| api | 8000 | ไม่เปิดในไฟล์หลัก; Local override ใช้ 8001 | FastAPI HTTP |
| db | 5432 | ไม่เปิดในไฟล์หลัก; Local override ใช้ 5433 | PostgreSQL |
| broker | 1883 | ไม่เปิดในไฟล์หลัก; Local override ใช้ 1883 | MQTT |
| simulator | - | - | Publishes fake telemetry inside Docker network |

## Startup Order

1. Compose starts `db`.
2. Docker runs `pg_isready` until `db` is healthy.
3. Compose starts `broker`.
4. Compose starts `api` after `db` is healthy and `broker` is started.
5. Docker checks `api` by calling `/health/ready` inside the API container.
6. Compose starts `simulator` after `api` is healthy.

`depends_on` controls startup order only. The application still needs readiness checks because a started process is not always ready to serve traffic.
