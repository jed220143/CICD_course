# Phase 14 Notes: Deploy from Registry

บทนี้เตรียม deploy โดยดึง image จาก GitHub Container Registry แทนการ build จาก source บนเครื่อง deploy

## New files

```text
infra/compose/compose.registry.yaml
scripts/deploy-registry-local.ps1
```

## Command

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\deploy-registry-local.ps1 -ImageTag v0.2.0
```

## Flow

```text
pull api/simulator images from GHCR
start db + broker
run Alembic migration from release image
start stack
health check through NGINX
```

## Why this matters

Local CD script เดิม build image จาก source:

```text
source code -> docker build -> run
```

Registry deploy ใช้ image ที่ CI/CD publish แล้ว:

```text
GHCR image -> docker pull -> run
```

นี่ใกล้ production มากกว่า เพราะ server ไม่ต้องมี build context หรือ build tools ครบ

## Current blocker observed

ตอนลอง pull:

```text
ghcr.io/jed220143/mini-telemetry-api:v0.2.0
ghcr.io/jed220143/mini-telemetry-simulator:v0.2.0
```

GHCR ตอบ:

```text
unauthorized
```

สาเหตุที่เป็นไปได้:

- GitHub Actions publish image ยังไม่สำเร็จ
- package ยังเป็น private
- Docker ยังไม่ได้ login กับ `ghcr.io`

ต้องตรวจใน GitHub Actions และ Packages ก่อน verify deploy จาก registry จริง
