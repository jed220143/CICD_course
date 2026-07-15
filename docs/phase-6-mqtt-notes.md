# Phase 6 Notes: MQTT Telemetry Ingest

สรุปบทนี้แบบเร็ว:

```text
simulator -> MQTT broker -> API subscriber -> PostgreSQL
```

## What changed

- เพิ่ม Mosquitto broker เป็น MQTT service สำหรับ local lab
- เพิ่ม simulator container ที่ publish telemetry จำลองของ `sensor-001`
- เพิ่ม API subscriber ด้วย `paho-mqtt`
- เพิ่ม `message_id` เพื่อกัน message ซ้ำ
- เพิ่ม Alembic migration `0002_message_id`

## Verified

- `pytest`: ผ่าน 2 tests
- `docker compose ps`: มี 4 containers
- `/health/ready`: `database: ok`
- API log: `Telemetry message processed: inserted=True`
- DB มีข้อมูลใน `telemetry_readings`

## Mental model

- Broker ไม่เก็บข้อมูลหลักของเรา แค่เป็นตัวกลางรับ/ส่ง message
- API เป็นตัวตัดสินใจว่าจะ validate/แปลง/บันทึกข้อมูลอย่างไร
- PostgreSQL เป็นที่เก็บข้อมูลถาวรผ่าน Docker named volume
