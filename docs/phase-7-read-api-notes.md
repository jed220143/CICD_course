# Phase 7 Notes: Read Telemetry API

บทนี้ทำให้ข้อมูลที่เก็บใน PostgreSQL “ถูกอ่านออกมาใช้ได้” ผ่าน HTTP API

## New endpoints

```text
GET /devices
GET /telemetry/latest?limit=3
GET /devices/sensor-001/readings?limit=3
```

## What each endpoint does

- `/devices`: ดู device ทั้งหมด พร้อมจำนวน readings
- `/telemetry/latest`: ดู telemetry ล่าสุดทุก device
- `/devices/{device_key}/readings`: ดู telemetry ของ device เดียว

## Verified

- `pytest`: ผ่าน 4 tests
- API container rebuild แล้ว healthy
- `/devices` เห็น `sensor-001`
- `/telemetry/latest?limit=3` คืนค่า telemetry ล่าสุดจาก DB จริง

## Mental model

Phase 6 คือข้อมูล “เข้า” ระบบ:

```text
simulator -> broker -> API -> DB
```

Phase 7 คือข้อมูล “ออก” จากระบบ:

```text
Browser/tool -> API -> DB -> JSON response
```
