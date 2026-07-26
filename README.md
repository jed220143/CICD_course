# Mini Telemetry Platform

โปรเจกต์ฝึก Cloud, CI/CD และ Container Infrastructure แบบ Project-Based โดยเพิ่มความซับซ้อนทีละ Phase และเน้นความเข้าใจมากกว่าการรันคำสั่งให้ผ่าน

## Current Status

- Phase 0–15: Local application, Docker, CI, GHCR และ Local CD ผ่านแล้ว
- Phase 16: AWS safety gate, IAM/MFA, EC2/SSH และ Docker Engine ผ่านแล้ว
- Application: FastAPI + PostgreSQL + MQTT + simulator + NGINX
- AWS EC2 Lab: หยุดเครื่องเมื่อพัก และต้อง Terminate หลังจบบท

## Learning Track

- Local-first และค่าใช้จ่ายจริงเป้าหมาย 0 บาท
- AWS Hands-on ใช้ได้เฉพาะเมื่อ Free Tier Gate ผ่าน
- Self-Signed HTTPS เรียนบน Local โดยไม่ซื้อ Domain
- ห้าม Commit Secret, Password, Token, Private Key หรือ `.env`

## Documents

- [Course plan](./Lesson%20plan/CODEX_CLOUD_CICD_COURSE_PLAN_TH.md)
- [Learning checklist](./Lesson%20plan/CODEX_CLOUD_CICD_LEARNING_CHECKLIST_TH.md)
- [Learning log](./docs/learning-log.md)
- [Cost safety policy](./docs/cost-safety.md)
- [AWS Free Tier gate](./docs/aws-free-tier-gate.md)
- [AWS EC2 deployment notes](./docs/phase-16-aws-ec2-notes.md)

## Development

Local build/deploy:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\deploy-local.ps1
```

Deploy release image จาก GHCR:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\deploy-registry-local.ps1 -ImageTag v0.2.0
```

Production-like/AWS ใช้ `infra/compose/compose.yaml` พร้อม env file ส่วน Local build/debug เพิ่ม `infra/compose/compose.local.yaml`
