# Phase 13 Notes: Release Tag

บทนี้ merge feature branch เข้า `main` แล้วสร้าง release tag

## Release tag

```text
v0.2.0
```

ชี้ไปที่ merge commit:

```text
cd8b96e Merge pull request #9 from jed220143/feature/mqtt-telemetry-ingest
```

## Why this matters

Git tag คือป้ายชื่อถาวรของ commit สำคัญ ใช้บอกว่า commit นี้คือ release/milestone ใด

เมื่อ push tag `v0.2.0` แล้ว GitHub Actions จะรัน workflow จาก trigger:

```yaml
push:
  tags:
    - "v*"
```

และ job `publish-images` จะ push image version tag ไป GHCR:

```text
ghcr.io/jed220143/mini-telemetry-api:v0.2.0
ghcr.io/jed220143/mini-telemetry-simulator:v0.2.0
```

## Verified locally before tag

- `main` fast-forward ตรงกับ `origin/main`
- `pytest`: ผ่าน 4 tests
- working tree สะอาด
