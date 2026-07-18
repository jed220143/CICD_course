# Learning Checklist

ใช้ไฟล์นี้เช็กว่าแต่ละบท “ผ่านพอไปต่อ” แล้ว ไม่ต้องละเอียดเกินไป ถ้าสงสัยค่อยย้อนถามเฉพาะจุด

## Completed

- [x] Phase 1: Git/GitHub workflow, branch, PR, merge, tag `v0.1.0`
- [x] Phase 2: FastAPI backend พร้อม `/health/live` และ `/health/ready`
- [x] Phase 3: Dockerize API และ publish port `8001:8000`
- [x] Phase 4: PostgreSQL + SQLAlchemy + Alembic migration + Docker volume
- [x] Phase 5: Compose core stack, network, healthcheck, `depends_on`
- [x] Phase 6: MQTT broker + simulator + API subscriber + telemetry insert เข้า DB
- [x] Phase 7: Read API สำหรับดู devices และ telemetry readings จาก DB
- [x] Local learning: bind mount ให้ simulator เขียนไฟล์ออกมาที่ `local-artifacts/simulator`
- [x] Phase 8: NGINX reverse proxy ผ่าน `localhost:8080`
- [x] Phase 9: GitHub Actions CI สำหรับ API tests และ Docker image build
- [x] Phase 10: GitHub Container Registry publish job สำหรับ image ที่ผ่าน CI
- [x] Phase 11: Local CD script สำหรับ build, migrate, start stack และ health check
- [x] Phase 12: Local application rollback เมื่อ deploy health check fail
- [x] Phase 13: Merge เข้า `main` และสร้าง release tag `v0.2.0`
- [ ] Phase 14: Deploy จาก GHCR image tag `v0.2.0`

## Current Stack

- `mini-telemetry-db`: PostgreSQL เก็บข้อมูลใน named volume
- `mini-telemetry-api`: FastAPI รับ HTTP และ subscribe MQTT
- `mini-telemetry-broker`: Mosquitto MQTT broker สำหรับ lab local
- `mini-telemetry-simulator`: ส่งข้อมูล sensor จำลองทุก 5 วินาที

## Phase 7 Pass Criteria

- [x] `GET /devices` แสดง device และจำนวน readings ได้
- [x] `GET /telemetry/latest?limit=3` แสดงข้อมูล telemetry ล่าสุดได้
- [x] `GET /devices/sensor-001/readings?limit=3` แสดงข้อมูลเฉพาะ device ได้
- [x] `pytest` ผ่าน 4 tests
- [x] API container healthy หลัง rebuild

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
