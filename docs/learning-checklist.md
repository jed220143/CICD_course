# Learning Checklist

ใช้ไฟล์นี้เช็กว่าแต่ละบท “ผ่านพอไปต่อ” แล้ว ไม่ต้องละเอียดเกินไป ถ้าสงสัยค่อยย้อนถามเฉพาะจุด

## Completed

- [x] Phase 1: Git/GitHub workflow, branch, PR, merge, tag `v0.1.0`
- [x] Phase 2: FastAPI backend พร้อม `/health/live` และ `/health/ready`
- [x] Phase 3: Dockerize API และ publish port `8001:8000`
- [x] Phase 4: PostgreSQL + SQLAlchemy + Alembic migration + Docker volume
- [x] Phase 5: Compose core stack, network, healthcheck, `depends_on`
- [x] Phase 6: MQTT broker + simulator + API subscriber + telemetry insert เข้า DB

## Current Stack

- `mini-telemetry-db`: PostgreSQL เก็บข้อมูลใน named volume
- `mini-telemetry-api`: FastAPI รับ HTTP และ subscribe MQTT
- `mini-telemetry-broker`: Mosquitto MQTT broker สำหรับ lab local
- `mini-telemetry-simulator`: ส่งข้อมูล sensor จำลองทุก 5 วินาที

## Phase 6 Pass Criteria

- [x] `docker compose ps` เห็น 4 containers
- [x] API `/health/ready` ตอบ `database: ok`
- [x] simulator publish message ไปที่ `devices/sensor-001/telemetry`
- [x] API log แสดง `Telemetry message processed: inserted=True`
- [x] PostgreSQL มี row ใน `telemetry_readings`

## Remember

- ลบ/recreate container ได้เมื่อ config/image เปลี่ยนหรือ container เสีย
- ห้ามลบ volume ถ้ายังต้องการข้อมูล DB
- `docker compose down` หยุด stack แต่ไม่ลบ volume
- `docker compose down -v` ลบ volume ด้วย ข้อมูล DB หาย
- commit/push ทำตอนจบบทหรือ milestone ไม่ต้องทำทุกขั้นย่อย
