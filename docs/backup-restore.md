# PostgreSQL Backup and Restore Runbook

## Backup

รันจาก PowerShell ที่ repository root:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\backup-db-local.ps1
```

Script จะ:

1. ใช้ `pg_dump --format=custom` ภายใน PostgreSQL container
2. ตรวจ catalog ด้วย `pg_restore --list`
3. copy dump ไป `local-artifacts/backups`
4. ตรวจว่าไฟล์ไม่ว่างและแสดง SHA256
5. เก็บ backup 7 วันโดยค่าเริ่มต้น

กำหนด retention ได้:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\backup-db-local.ps1 -RetentionDays 14
```

## Restore verification

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\verify-db-restore-local.ps1
```

Script จะเลือก backup ล่าสุด สร้าง Database ชั่วคราว แยกจาก `telemetry`, restore, ตรวจ migration/device/telemetry rows แล้วลบเฉพาะ Database ทดสอบ

เลือกไฟล์เองได้:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\verify-db-restore-local.ps1 `
  -BackupPath .\local-artifacts\backups\telemetry-YYYYMMDD-HHMMSS.dump
```

## Safety

- Backup ไม่หยุด live Database
- Restore drill ไม่เขียนทับ Database `telemetry`
- `local-artifacts` ไม่ถูก commit
- Dump อาจมีข้อมูลจริงและต้องเข้ารหัส/จำกัดสิทธิ์ใน Production
- Backup ที่ไม่เคยผ่าน restore test ยังไม่ถือว่าเชื่อถือได้

## Verified result

วันที่ 2026-07-29:

```text
Format: PostgreSQL custom dump
Migration: 0002_message_id
Devices restored: 1
Telemetry readings restored: 4590
Restore result: PASS
```
