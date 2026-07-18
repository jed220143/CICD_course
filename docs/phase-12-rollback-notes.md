# Phase 12 Notes: Local Rollback

บทนี้เพิ่ม rollback เบื้องต้นให้ `scripts/deploy-local.ps1`

## What rollback means here

ถ้า deploy image ใหม่แล้ว health check ไม่ผ่าน script จะพยายามถอยกลับไปใช้ image เก่า:

```text
mini-telemetry-api:rollback
mini-telemetry-simulator:rollback
```

## Flow

```text
save current api/simulator images as rollback tags
build new images
run migration
start stack
health check
if health fails -> restore rollback image tags -> restart app services
```

## Important limitation

rollback นี้เป็น application image rollback เท่านั้น

```text
DB schema is not downgraded automatically
```

เหตุผลคือ database rollback เสี่ยงกว่า image rollback มาก เช่น column ใหม่อาจมีข้อมูลใหม่แล้ว ถ้าลบ column ทันทีข้อมูลอาจหาย

## Production lesson

deploy ที่ดีควรมี:

- health check
- rollback path
- migration strategy
- logs/evidence เมื่อ deploy fail

ตอนนี้เราเริ่มมี health check และ rollback path แล้วใน local CD

## Verification

- `pytest`: ผ่าน 4 tests
- `scripts/deploy-local.ps1`: deploy ปกติผ่าน
- script สร้าง rollback tags ก่อน build:
  - `mini-telemetry-api:rollback`
  - `mini-telemetry-simulator:rollback`
