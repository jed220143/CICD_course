# Phase 15 Notes: Compose Hardening

บทนี้แยก config หลักออกจากของ local-only

## Files

```text
infra/compose/compose.yaml
infra/compose/compose.registry.yaml
infra/compose/compose.local.yaml
```

## What changed

ไฟล์หลัก `compose.yaml` และ `compose.registry.yaml` เหลือ exposed port หลักแค่ NGINX:

```text
8080:80
```

ย้ายของ dev/debug ไป `compose.local.yaml`:

```text
broker port 1883
db port 5433
api port 8001
simulator local-artifacts bind mount
```

## Why this matters

production-minded compose ไม่ควรเปิด DB/API/Broker ออก host ถ้าไม่จำเป็น

```text
user/tool -> nginx -> api -> db/broker internal network
```

DB, API และ broker ยังสื่อสารกันได้ผ่าน Docker network แต่ host ภายนอกเห็นแค่ NGINX

## Commands

Production-like local deploy:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\deploy-registry-local.ps1 -ImageTag v0.2.0
```

Local debugging with extra ports/artifacts:

```powershell
docker compose -f infra\compose\compose.yaml -f infra\compose\compose.local.yaml up -d
```

## Key idea

```text
compose.yaml = core deploy shape
compose.local.yaml = local convenience
```
