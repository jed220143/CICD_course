# Phase 16 Notes: AWS EC2 Deployment Preparation

บทนี้เตรียม EC2 แบบ Free-first และจัด Compose ให้ Local กับ AWS ใช้โครงสร้างระบบร่วมกัน

## Compose ที่ใช้จริง

```text
infra/compose/compose.yaml        # release/AWS shape
infra/compose/compose.local.yaml  # build, debug ports, local artifacts
```

ไม่มี Compose แยกสำหรับ registry หรือ AWS เพราะ environment และ image tag เพียงพอสำหรับความแตกต่างนี้

## Local

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\deploy-local.ps1
```

Script จะเพิ่ม local override, build source และใช้รหัส DB สำหรับข้อมูลจำลองเฉพาะเครื่อง

## AWS/Ubuntu

สร้าง secret file บน EC2 โดยไม่ใส่ค่าจริงลง Git:

```bash
cd ~/CICD_course/infra/compose
umask 077
printf 'IMAGE_TAG=v0.2.0\nPOSTGRES_PASSWORD=%s\n' "$(openssl rand -hex 24)" > .env.aws
chmod 600 .env.aws
```

Deploy:

```bash
cd ~/CICD_course
bash scripts/deploy-registry-linux.sh v0.2.0
```

Flow:

```text
validate config -> pull images -> start DB/broker
-> Alembic migration -> start stack -> NGINX health check
```

## Security boundary ของ Lab

- Security Group เปิด SSH `22` และ Lab `8080` จาก My IP เท่านั้น
- DB, API และ MQTT broker ไม่เปิด host port บน AWS
- `.env.aws` และ `.pem` ห้าม commit
- Mosquitto anonymous ใช้ได้เพราะ broker อยู่ใน internal Docker network สำหรับ Lab; production จริงต้องเพิ่ม authentication/TLS
- Public HTTPS, managed secrets และ automatic rollback เป็นบทถัดไป ไม่ควรอ้างว่าระบบปัจจุบัน production-ready เต็มรูปแบบ

## Cost stop

- พักชั่วคราวใช้ Stop; EBS ยังอยู่และ Public IPv4 อาจเปลี่ยน
- จบบทใช้ Terminate แล้วตรวจ EBS, Public/Elastic IP, Billing และ Credits
