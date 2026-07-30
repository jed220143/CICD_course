# Incident Report: PostgreSQL Stopped

## Summary

ทดลองหยุด PostgreSQL container แบบควบคุมเพื่อพิสูจน์ Monitoring และ Recovery flow บน Local stack

## Impact

- API process ยังรัน แต่ `/health/ready` ตอบ `503`
- API Docker health เปลี่ยนเป็น `unhealthy`
- Simulator ยังส่ง MQTT แต่ API ไม่สามารถบันทึก telemetry ลง DB ระหว่าง outage
- Read API ใช้งานไม่ได้จนกว่า DB จะกลับมา

## Detection

- Grafana `Database Readiness` เปลี่ยน `UP → DOWN`
- Prometheus ยัง scrape API ได้ จึงเห็นความแตกต่างระหว่าง `up=1` กับ application readiness
- Docker status และ API health endpoint ยืนยันอาการ

## Root cause

PostgreSQL container ถูกสั่ง `stop` ระหว่าง controlled incident drill ไม่ใช่ application defect หรือ data corruption

## Recovery

1. สั่ง `docker compose start db`
2. รอ PostgreSQL health check ผ่าน
3. เรียก `/health/ready` ได้ `200` และ `database=ok`
4. Grafana กลับเป็น `UP`
5. ตรวจข้อมูล telemetry แล้วยังอยู่ใน named volume เดิม

## Prevention and production controls

- Alert เมื่อ readiness เป็น 0 ต่อเนื่องตามเวลาที่กำหนด
- ใช้ `restart: unless-stopped` สำหรับ unexpected process exit
- เก็บ PostgreSQL backup และทำ restore drill
- ตรวจ disk, memory และ PostgreSQL logs ก่อน restart ซ้ำ
- ไม่ใช้ `docker compose down -v` ระหว่างแก้ incident

## O-H-T-F

- Observe: Dashboard DOWN, readiness 503, API unhealthy
- Hypothesize: DB container หยุดหรือเชื่อมต่อ DB ไม่ได้
- Test: ตรวจ `docker compose ps` และเรียก `/health/ready`
- Fix and Verify: start DB, รอ healthy, ตรวจ dashboard/API/data ซ้ำ
