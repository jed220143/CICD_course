# Phase 13 Notes: Prometheus และ Grafana

บทนี้เพิ่ม Metrics และ Local Monitoring Stack ตามแผน Phase 13 โดยยังไม่นำ Grafana ขึ้น EC2 เครื่องเล็ก

## Data flow

```text
FastAPI /metrics
      ↓ scrape ทุก 5 วินาที
Prometheus
      ↓ PromQL query
Grafana dashboard
```

Grafana ไม่ได้อ่านข้อมูลจาก API หรือ PostgreSQL โดยตรง แต่ใช้ Prometheus เป็น data source

## Metrics ที่เพิ่ม

- `http_requests_total`: จำนวน HTTP request แยกตาม method, route และ status
- `http_request_duration_seconds`: ระยะเวลาตอบ HTTP request
- `mqtt_messages_received_total`: จำนวน MQTT message ที่ API ได้รับ
- `mqtt_invalid_payloads_total`: payload ที่ decode ไม่ได้
- `telemetry_inserted_total`: telemetry ที่บันทึกลง DB สำเร็จ
- `telemetry_duplicates_total`: message ID ที่ซ้ำและไม่ insert ซ้ำ
- `telemetry_database_failures_total`: การเขียน telemetry ลง DB ที่ล้มเหลว

## Local services

Prometheus และ Grafana อยู่ใน `compose.local.yaml` เท่านั้น:

```text
http://localhost:9090  Prometheus
http://localhost:3000  Grafana
```

Grafana login เริ่มต้นใช้ `admin` / `admin` และจะให้ตั้งรหัสใหม่เมื่อเข้าใช้ครั้งแรก

Dashboard ถูก provision ไว้ที่:

```text
Dashboards → Mini Telemetry → Mini Telemetry Overview
```

## Start

เปิด Docker Desktop แล้ว deploy local:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\deploy-local.ps1
```

ตรวจตามลำดับ:

1. `http://localhost:8001/metrics` เห็น Prometheus text format
2. `http://localhost:9090/targets` เห็น `mini-telemetry-api` เป็น `UP`
3. `http://localhost:3000` เปิด dashboard ได้

## Persistence

- Prometheus เก็บ time series ใน named volume `prometheus_data`
- Grafana เก็บ state ใน named volume `grafana_data`
- `docker compose down` ไม่ลบข้อมูล
- `docker compose down -v` ลบข้อมูล monitoring และ database volumes จึงห้ามใช้โดยไม่ตั้งใจ

## Current verification

- API tests ผ่าน 5 tests รวม `/metrics`
- Compose base + local override ผ่าน config validation
- Dashboard JSON parse ผ่าน
- Prometheus target `mini-telemetry-api` เป็น `UP`
- Grafana health ตอบ `database: ok`
- `mqtt_messages_received_total` และ `telemetry_inserted_total` เพิ่มตาม Simulator จริง
- ผู้เรียนสร้าง DB readiness และ FastAPI process CPU panels ใน Grafana ด้วยตนเอง
- หยุด PostgreSQL แบบควบคุมแล้ว readiness เปลี่ยน `UP → DOWN`; หลัง start กลับมา API healthy, readiness `UP` และข้อมูลใน volume ยังอยู่

### Incident ระหว่างเปิด Local stack

Simulator restart loop เพราะไฟล์ output เก่าถูกสร้างโดย root ก่อนเปลี่ยน image ให้รันด้วย non-root user:

```text
PermissionError: /app/out/latest-telemetry.json
```

เก็บไฟล์เก่าไว้ด้วยชื่อ `.pre-nonroot.*` แล้วให้ user `app` สร้าง output ชุดใหม่ หลังแก้ Simulator กลับมา publish และ metrics เพิ่มตามปกติ

## Log management

- HTTP response มี `X-Request-ID`
- API log มี request ID, method, route, status และ duration
- Docker ใช้ `json-file` พร้อม `max-size=10m`, `max-file=3`
- Application เขียน stdout/stderr; Docker เป็นผู้เก็บและ rotate

## Backup, restore และ incident

- Backup runbook: `docs/backup-restore.md`
- Incident report: `docs/incident-report.md`
- Restore drill ผ่านกับ migration `0002_message_id`, device 1 ตัว และ telemetry 4,590 แถว
