# Phase 11 Notes: Local CD

บทนี้เริ่มฝั่ง CD แบบ local ก่อน ยังไม่แตะ AWS และยังไม่เสียเงิน

## Script

```text
scripts/deploy-local.ps1
```

## Deploy flow

```text
build api/simulator images
start db + broker
run Alembic migration
start full stack
health check through NGINX
```

## Why migration moved into API image

ก่อนหน้านี้ API image มีแค่ app code แต่ไม่มี:

```text
alembic.ini
api/alembic/
```

ดังนั้น production-like deploy จะรัน migration จาก image ไม่ได้

ตอนนี้ `api/Dockerfile` copy migration files เข้า image แล้ว ทำให้คำสั่งนี้ทำงานได้จาก container:

```text
python -m alembic upgrade head
```

## CI vs Registry vs CD

```text
CI = test/build ว่าผ่านไหม
Registry = เก็บ image ที่ผ่านแล้ว
CD = เอา image/code ที่ผ่านแล้วไปรัน พร้อม migrate + health check
```

## Current scope

เป็น Local CD ยังไม่ใช่ production cloud deploy แต่ flow ใกล้ของจริงขึ้น:

- มี migration step
- มี start stack step
- มี health check
- ถ้า health ไม่ ready script fail

## Verification

- `pytest`: ผ่าน 4 tests
- `scripts/deploy-local.ps1`: build, migrate, start stack และ health check ผ่าน
- แก้ deploy script ให้ตรวจ `$LASTEXITCODE` หลัง `docker compose` ทุกครั้ง เพื่อไม่ให้ health check ของ stack เก่าหลอกว่า deploy สำเร็จ

## Next improvement

Phase 12 เพิ่ม application image rollback เมื่อ health check ของ deploy ใหม่ไม่ผ่าน
