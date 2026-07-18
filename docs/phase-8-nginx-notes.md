# Phase 8 Notes: NGINX Reverse Proxy

บทนี้เพิ่ม NGINX เป็นประตูหน้าให้ระบบ

```text
Browser/tool -> localhost:8080 -> nginx -> api:8000 -> PostgreSQL
```

## New URL shape

เดิมยิง API ตรง:

```text
http://127.0.0.1:8001/health/ready
```

ผ่าน NGINX:

```text
http://127.0.0.1:8080/api/health/ready
```

## Key idea

- `nginx` กับ `api` อยู่ใน Docker network เดียวกัน
- NGINX เรียก API ด้วย service name: `api:8000`
- Host เห็นแค่ port `8080`
- ใน production มักให้ user เข้า NGINX/Load Balancer ก่อน ไม่ยิง backend ตรง

## Config file

```text
infra/nginx/default.conf
```

ถูก mount เข้า container แบบ read-only:

```text
../nginx/default.conf:/etc/nginx/conf.d/default.conf:ro
```
