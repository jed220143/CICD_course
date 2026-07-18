# Phase 10 Notes: Container Registry

บทนี้เพิ่มขั้น “เก็บ Docker image ที่ build ผ่านแล้ว” ไว้ใน GitHub Container Registry หรือ GHCR

## Registry คืออะไร

```text
GitHub repo = เก็บ source code
Container registry = เก็บ Docker image
```

## Image names

```text
ghcr.io/jed220143/mini-telemetry-api
ghcr.io/jed220143/mini-telemetry-simulator
```

## Workflow behavior

PR และ feature branch:

```text
run tests
build images
ไม่ push image
```

main, tag `v*`, หรือ manual run:

```text
run tests
build images
push images to GHCR
```

## Tags

- `sha-<commit_sha>` = immutable tag ใช้อ้างอิง commit ที่แน่นอน
- `latest` = อัปเดตเฉพาะตอน push เข้า `main`
- `v1.2.3` = อัปเดตเฉพาะตอนสร้าง Git tag

## Why this matters

- deploy server ไม่ต้อง build จาก source code เอง
- rollback ง่ายกว่า เพราะเลือก image tag เก่าได้
- ทุก environment ใช้ image เดียวกัน
- CI build ครั้งเดียว แล้ว CD ดึง image ที่ผ่านแล้วไป deploy

## Current scope

ตอนนี้ยังไม่ deploy และยังไม่แตะ AWS เป็นแค่เตรียม artifact สำหรับ CD ขั้นถัดไป
