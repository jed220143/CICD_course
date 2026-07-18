# Phase 9 Notes: GitHub Actions CI

บทนี้เพิ่ม CI ให้ GitHub ตรวจงานอัตโนมัติเมื่อมี `push` หรือ `pull_request`

## Workflow file

```text
.github/workflows/ci.yml
```

## CI jobs

```text
api-tests
  -> checkout
  -> setup Python 3.11
  -> install api[dev]
  -> run pytest

docker-build
  -> checkout
  -> docker build api
  -> docker build simulator
```

## Why this matters

- ไม่เชื่อแค่เครื่องเรา
- PR ต้องมีหลักฐานว่า test ผ่านบน clean runner
- Dockerfile พังจะรู้ก่อน merge
- ยังไม่ deploy และยังไม่เสียเงิน

## CI vs CD

- CI = ตรวจว่า code/test/build ผ่าน
- CD = เอาสิ่งที่ผ่านแล้วไป deploy

ตอนนี้เราทำ CI ก่อน ยังไม่ทำ CD
