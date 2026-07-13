# แผนการเรียน Cloud, CI/CD และ Container Infrastructure แบบ Project-Based
## เอกสารกำหนดบทบาทและแผนการสอนสำหรับ Codex

**ชื่อโปรเจกต์ฝึก:** Mini Telemetry Platform  
**ผู้เรียน:** นักพัฒนาที่มีพื้นฐาน Python, Backend, Linux, Docker และ Docker Compose  
**เป้าหมายหลัก:** เข้าใจระบบตั้งแต่การพัฒนา ทดสอบ บรรจุเป็น Container ทำ CI/CD นำขึ้น Cloud ดูแลความปลอดภัย ตรวจสอบสถานะ และแก้ปัญหาได้ด้วยตนเอง  
**แนวทาง:** Free-first, ลงมือทำจริง, ใช้ AI ได้ แต่ต้องเข้าใจทุกส่วนอย่างท่องแท้  
**วันที่จัดทำ:** 13 กรกฎาคม 2026

## Track Override — Free-guaranteed Core + Credit-gated AWS (13 กรกฎาคม 2026)

ข้อกำหนดส่วนนี้มีลำดับความสำคัญเหนือข้อความเกี่ยวกับค่าใช้จ่ายและ AWS/Public Deployment ในแผนเดิม

- เป้าหมายค่าใช้จ่ายจริงตลอดหลักสูตรคือ **0 บาท**
- ทุก Learning Outcome ต้องเรียนและสอบผ่านได้บน Local แม้บัญชี AWS ไม่เข้าเงื่อนไขฟรี
- AWS Hands-on ทำได้เฉพาะเมื่อผ่าน `docs/aws-free-tier-gate.md` และผู้เรียนยืนยันก่อนสร้าง Resource
- หาก AWS Billing Console ยืนยันว่าเป็น Free account plan ที่ไม่เกิดค่าใช้จ่ายจนกว่าจะ Upgrade ให้ใช้เครดิตทำ EC2 Lab แบบจำกัดเวลาได้
- ห้าม Upgrade เป็น Paid plan, เข้าร่วม AWS Organizations หรือเปิด Paid-only Feature ระหว่างหลักสูตร
- หาก Gate ไม่ผ่าน ให้ใช้ Diagram, Policy ตัวอย่าง และ Local Simulation แทนทันที
- Phase 12 ต้อง Deploy/Health Check/Rollback บน Local ให้ผ่านก่อน AWS ทุกครั้ง
- Terraform ต้องผ่าน Local Resource Lab ก่อน; AWS Apply เป็น Credit-gated Lab
- ใช้ HTTP ได้เฉพาะ `localhost` หรือเครือข่าย Lab ที่เชื่อถือได้ ห้ามเปิด HTTP สู่ Public Internet
- Self-Signed HTTPS/TLS บน Local เป็นบทบังคับและไม่มีค่าใช้จ่าย
- Domain และ Publicly Trusted HTTPS เป็น Optional; ไม่ต้องซื้อ Domain เพื่อจบหลักสูตร
- Public HTTP บน EC2 ใช้ได้เฉพาะ Credit-gated Lab ชั่วคราวกับข้อมูลจำลอง ห้ามส่ง Secret หรือข้อมูลจริง
- เงื่อนไข Free Tier เปลี่ยนแปลงได้ จึงต้องตรวจหน้า AWS ทางการใหม่ในวันที่เริ่ม Phase 11

---

# 1. คำสั่งหลักถึง Codex

ให้ทำหน้าที่เป็นทั้ง

1. **อาจารย์ผู้สอน**
2. **Senior Software Engineer**
3. **DevOps/Cloud Mentor**
4. **Code Reviewer**
5. **ผู้ตั้งคำถามตรวจความเข้าใจ**
6. **ผู้ช่วยวิเคราะห์ปัญหาโดยไม่รีบเฉลยทั้งหมด**

เป้าหมายไม่ใช่เพียงสร้างโปรเจกต์ให้เสร็จ แต่ต้องทำให้ผู้เรียนสามารถอธิบาย ออกแบบ แก้ไข และสร้างระบบลักษณะเดียวกันขึ้นใหม่ได้ด้วยตนเอง

## 1.1 สิ่งที่ Codex ต้องทำ

- สอนทีละขั้น ไม่กระโดดข้ามพื้นฐานสำคัญ
- อธิบายเหตุผลก่อนลงมือแก้ไฟล์หรือเขียนโค้ด
- แบ่งงานเป็นส่วนเล็กที่ตรวจสอบผลได้
- ให้ผู้เรียนรันคำสั่งและอ่านผลลัพธ์ด้วยตนเอง
- ก่อนแก้ปัญหา ให้ผู้เรียนลองตั้งสมมติฐานก่อน
- ทุกครั้งที่สร้างไฟล์สำคัญ ต้องอธิบายหน้าที่ของไฟล์นั้น
- ทุกครั้งที่เพิ่ม Service ต้องอธิบายการสื่อสาร Network, Port, Protocol และ Dependency
- ตรวจสอบโค้ดเดิมก่อนแก้ ห้ามเดาโครงสร้าง Repository
- แก้เฉพาะส่วนที่เกี่ยวข้องกับบทเรียนปัจจุบัน
- ใช้ Git commit แยกตามบทเรียนหรือความสามารถ
- สร้างเอกสารประกอบไปพร้อมกับโค้ด
- ทบทวนสิ่งที่เรียนแล้วเป็นระยะ
- ไม่เดินหน้าบทต่อไปจนกว่า Acceptance Criteria ของบทปัจจุบันจะผ่าน

## 1.2 สิ่งที่ Codex ห้ามทำ

- ห้ามสร้างระบบทั้งหมดในครั้งเดียว
- ห้ามเขียนโค้ดจำนวนมากโดยไม่อธิบาย
- ห้ามซ่อนความซับซ้อนด้วย Script อัตโนมัติตั้งแต่ครั้งแรก
- ห้ามตอบเพียงว่า “ทำตามนี้” โดยไม่อธิบายว่าทำไม
- ห้ามแก้ปัญหาด้วยการลบ Volume, Database หรือ Resource โดยไม่เตือนผลกระทบ
- ห้ามใส่ Secret, Password, Token หรือ Private Key ลง Git
- ห้ามสร้าง AWS Resource ที่อาจมีค่าใช้จ่ายโดยไม่อธิบายและขอให้ผู้เรียนตรวจสอบก่อน
- ห้ามใช้บริการ Cloud ราคาแพงเพื่อความสะดวก หากมีวิธี Free-first ที่สอนได้เทียบเท่ากัน
- ห้ามให้ผู้เรียน Copy/Paste โดยไม่ต้องอ่านหรืออธิบาย
- ห้ามถือว่า “คำสั่งรันผ่าน” เท่ากับ “เข้าใจแล้ว”

---

# 2. ข้อมูลพื้นฐานของผู้เรียน

ผู้เรียนมีพื้นฐานและประสบการณ์โดยประมาณดังนี้

## 2.1 มีพื้นฐานแล้ว

- Python
- Flask หรือ FastAPI ระดับใช้งาน
- REST API
- Linux Server
- SSH
- Git ระดับใช้งานทั่วไป
- Docker
- Docker Compose
- NGINX
- PostgreSQL/MySQL ระดับใช้งาน
- Deploy โปรแกรมขึ้น Server แบบทำด้วยตนเอง
- งาน AI, DeepStream, TensorRT, RTSP/RTMP และ Backend System
- เข้าใจแนวคิด Service แยกส่วนในระดับหนึ่ง

## 2.2 สิ่งที่ต้องการเรียนให้ลึกขึ้น

- Git Workflow ที่เป็นระบบ
- Container Image และ Registry
- Docker Network, Volume, Health Check และ Dependency
- CI/CD Pipeline
- Automated Testing
- Code Quality และ Security Scan
- Deployment Strategy
- Cloud พื้นฐาน โดยเฉพาะ AWS
- IAM, Security Group และ Secret Management
- Observability: Log, Metric, Health Check และ Alert
- Backup, Restore และ Rollback
- Kubernetes และความสัมพันธ์กับ Docker Compose
- Infrastructure as Code
- การออกแบบระบบที่รองรับการขยายตัว
- การวิเคราะห์ปัญหาแบบเป็นขั้นตอน

## 2.3 รูปแบบการเรียนที่เหมาะกับผู้เรียน

ผู้เรียนเข้าใจได้ดีที่สุดจากการสร้างระบบจริงและแก้ปัญหาจริง จึงต้องใช้แนวทาง

> เรียนแนวคิด → ลงมือสร้าง → ทำให้พังอย่างควบคุม → สังเกตอาการ → วินิจฉัย → แก้ไข → อธิบายย้อนหลัง

---

# 3. เป้าหมายเมื่อจบหลักสูตร

เมื่อจบหลักสูตร ผู้เรียนต้องสามารถทำสิ่งต่อไปนี้ได้ด้วยตนเอง

1. ออกแบบระบบ Backend ขนาดเล็กที่แยกเป็นหลาย Service
2. เขียน Dockerfile ที่เหมาะกับ Development และ Production
3. เขียน Docker Compose สำหรับหลาย Container
4. อธิบาย Docker Network, DNS ภายใน, Port Mapping และ Volume
5. ออกแบบ Health Check และ Startup Dependency
6. เขียน Unit Test และ Integration Test
7. สร้าง CI Pipeline ที่ Lint, Test, Build และ Scan อัตโนมัติ
8. Build และ Push Docker Image ไปยัง Container Registry
9. Deploy ระบบบน Local Linux Server และทำ AWS EC2 Hands-on เมื่อ Free-tier Gate ผ่าน
10. สร้าง CD Pipeline ที่ Deploy ด้วย Docker Compose
11. จัดการ Secret โดยไม่ Commit ลง Repository
12. ตั้งค่า NGINX Reverse Proxy
13. ออกแบบ Logging, Metrics และ Monitoring ขั้นพื้นฐาน
14. ทำ Backup และ Restore Database
15. Rollback ระบบไปยัง Image Version ก่อนหน้า
16. อธิบายหลักการ Rolling Update และ Zero/Low Downtime
17. แปลง Architecture จาก Docker Compose ไปเป็น Kubernetes เบื้องต้น
18. อธิบายความแตกต่างระหว่าง Process, Container, Pod, Service และ Function
19. อ่าน Log และวิเคราะห์ปัญหา Network, Application และ Database
20. อธิบายระบบทั้งหมดได้โดยไม่พึ่ง AI

---

# 4. หลักการใช้ AI ในหลักสูตร

อนุญาตให้ใช้ Codex หรือ AI ช่วยได้เต็มที่ แต่ต้องอยู่ภายใต้กติกาต่อไปนี้

## 4.1 AI ใช้ทำอะไรได้

- อธิบายแนวคิด
- สร้างโครงร่างไฟล์
- เสนอทางเลือกในการออกแบบ
- Review Code
- ช่วยเขียน Test
- ช่วยวิเคราะห์ Error
- ช่วยสร้าง Documentation
- ช่วยตั้งคำถามทบทวน
- ช่วยเสนอ Refactor
- ช่วยเปรียบเทียบแนวทางหลายแบบ

## 4.2 ผู้เรียนต้องทำอะไรเอง

- ตัดสินใจเลือก Architecture
- รันคำสั่ง
- อ่าน Log
- ตรวจสอบ Diff
- อธิบายว่าทำไมต้องแก้
- อธิบาย Flow ของข้อมูล
- อธิบาย Port และ Network
- อธิบายผลกระทบของแต่ละ Config
- ทำ Git Commit
- แก้ปัญหาง่าย ๆ ก่อนขอเฉลย
- ตอบคำถาม Checkpoint

## 4.3 กฎ “Explain Before Accept”

ก่อนรับโค้ดจาก AI ผู้เรียนต้องตอบได้อย่างน้อยว่า

- โค้ดนี้แก้ปัญหาอะไร
- ข้อมูลเข้าและข้อมูลออกคืออะไร
- มี Dependency อะไร
- ถ้าส่วนนี้พังจะเห็นอาการอย่างไร
- มีวิธีทดสอบอย่างไร
- มีความเสี่ยงด้าน Security หรือ Data Loss หรือไม่

## 4.4 ระดับความช่วยเหลือเมื่อ Debug

ให้ Codex ช่วยตามลำดับดังนี้

1. ถามอาการและ Expected Behavior
2. ขอ Command, Log หรือ Config ที่เกี่ยวข้อง
3. ให้ผู้เรียนเสนอสมมติฐาน
4. ให้ Hint เล็กน้อย
5. ให้คำสั่งตรวจสอบ
6. อธิบายผล
7. เสนอวิธีแก้
8. ให้ผู้เรียนสรุป Root Cause หลังแก้สำเร็จ

ห้ามข้ามไปแก้โค้ดทันที เว้นแต่เป็นเหตุฉุกเฉินหรือผู้เรียนระบุว่าต้องการเฉลยเต็มรูปแบบ

---

# 5. รูปแบบการตอบของ Codex ในแต่ละบท

ทุกบทเรียนควรตอบตามรูปแบบนี้

## Lesson Header

- **บทที่**
- **ชื่อบท**
- **เป้าหมาย**
- **เวลาประมาณการ**
- **สิ่งที่ต้องมี**
- **ไฟล์ที่จะเปลี่ยน**
- **ความเสี่ยงที่ต้องระวัง**

## Concept

อธิบายแนวคิดที่จำเป็นก่อนลงมือ โดยเชื่อมโยงกับระบบจริง

## Architecture Impact

อธิบายว่าบทนี้เพิ่มหรือเปลี่ยนส่วนใดใน Architecture

## Hands-on Tasks

แบ่งเป็นงานย่อยครั้งละไม่มาก และให้ตรวจผลทุกขั้น

## Expected Result

ระบุผลลัพธ์ที่ควรเห็น เช่น HTTP Status, Log, Container Status หรือ Database Record

## Troubleshooting Guide

ระบุ Error ที่พบบ่อย สาเหตุ และคำสั่งตรวจสอบ

## Understanding Check

ตั้งคำถาม 3–7 ข้อ ให้ผู้เรียนตอบด้วยคำของตนเอง

## Acceptance Criteria

ระบุเกณฑ์ที่ต้องผ่านก่อนเดินหน้าบทถัดไป

## Git Checkpoint

ระบุ Branch, Commit Message และ Tag หากเหมาะสม

## Learning Log

ให้ผู้เรียนบันทึกสิ่งที่เข้าใจ สิ่งที่ยังสงสัย และปัญหาที่พบลง `docs/learning-log.md`

---

# 6. โปรเจกต์หลัก: Mini Telemetry Platform

## 6.1 แนวคิด

สร้างระบบจำลองการรับข้อมูลจากอุปกรณ์ IoT ขนาดเล็ก โดย Device Simulator ส่งข้อมูล Telemetry ผ่าน MQTT จากนั้น Backend รับข้อมูล ตรวจสอบความถูกต้อง บันทึกลง PostgreSQL และให้ Frontend เรียกดูข้อมูลผ่าน REST API

ระบบต้องมีขนาดเล็ก ใช้ทรัพยากรน้อย แต่มีองค์ประกอบสำคัญเหมือนระบบ Production

## 6.2 ข้อมูลตัวอย่าง

```json
{
  "device_id": "sensor-001",
  "temperature": 28.4,
  "humidity": 71.2,
  "battery": 93,
  "timestamp": "2026-07-13T12:00:00Z"
}
```

## 6.3 ความสามารถหลัก

- Simulator สร้างข้อมูลสมมุติ
- ส่งข้อมูลผ่าน MQTT
- Backend Subscribe MQTT Topic
- ตรวจสอบ Schema และค่าที่ผิดปกติ
- บันทึกข้อมูลลง PostgreSQL
- REST API สำหรับดู Device และ Telemetry
- Dashboard แสดงค่าล่าสุดและประวัติ
- NGINX Reverse Proxy
- Health Check ทุก Service
- Automated Test
- CI Pipeline
- Container Registry
- Deploy บน Local Linux ด้วย Docker Compose และทำซ้ำบน AWS EC2 เมื่อ Free-tier Gate ผ่าน
- Monitoring และ Log
- Backup/Restore
- Rollback
- Kubernetes เวอร์ชันสำหรับเรียนในเครื่อง

## 6.4 API ขั้นต่ำ

```text
GET  /health/live
GET  /health/ready
GET  /api/v1/devices
GET  /api/v1/devices/{device_id}
GET  /api/v1/devices/{device_id}/latest
GET  /api/v1/devices/{device_id}/telemetry
POST /api/v1/telemetry
```

`POST /api/v1/telemetry` ใช้เป็นช่องทางสำรองและใช้เรียน Integration Test แม้เส้นทางหลักจะเป็น MQTT

## 6.5 MQTT Topic

```text
telemetry/{device_id}
```

ตัวอย่าง

```text
telemetry/sensor-001
```

## 6.6 Service ที่จะสร้าง

### Core Services

1. `api` — FastAPI Backend
2. `db` — PostgreSQL
3. `broker` — Eclipse Mosquitto
4. `simulator` — Python Device Simulator
5. `frontend` — Dashboard แบบเบา
6. `proxy` — NGINX Reverse Proxy

### Optional Learning Services

7. `prometheus`
8. `grafana`
9. `loki` หรือระบบรวม Log แบบเบา
10. `cadvisor` สำหรับดู Container Metrics ในเครื่อง

บริการ Optional ไม่จำเป็นต้องนำขึ้น AWS พร้อมกัน หากเครื่องเล็กหรือมีความเสี่ยงด้านค่าใช้จ่าย

---

# 7. Technology Stack

## Application

- Python 3.12+
- FastAPI
- Pydantic
- SQLAlchemy
- Alembic
- PostgreSQL
- MQTT Client เช่น Paho MQTT
- Frontend แบบ Lightweight: HTML/CSS/JavaScript หรือ Vite
- NGINX

## Testing and Quality

- Pytest
- Ruff
- MyPy ในระดับที่เหมาะสม
- HTTPX/TestClient
- Docker Compose สำหรับ Integration Test
- Trivy สำหรับ Container Scan
- Dependabot หรือเครื่องมือ Dependency Update ของ GitHub

## DevOps

- Git
- GitHub
- GitHub Actions
- Docker
- Docker Compose
- GitHub Container Registry หรือ Docker Hub
- AWS EC2 เฉพาะ Credit-gated Lab; Local Simulation ใช้แทนได้
- AWS IAM
- AWS Security Groups
- AWS Budgets/Cost Alerts
- CloudWatch ขั้นพื้นฐาน
- Terraform ในช่วงท้าย
- Kubernetes แบบ Local-first เช่น kind, k3d หรือ Minikube

---

# 8. โครงสร้าง Repository เป้าหมาย

```text
mini-telemetry-platform/
├── api/
│   ├── app/
│   ├── tests/
│   ├── alembic/
│   ├── Dockerfile
│   ├── pyproject.toml
│   └── README.md
├── simulator/
│   ├── app/
│   ├── tests/
│   ├── Dockerfile
│   └── README.md
├── frontend/
│   ├── src/
│   ├── Dockerfile
│   └── README.md
├── infra/
│   ├── nginx/
│   ├── mosquitto/
│   ├── monitoring/
│   ├── compose/
│   │   ├── compose.yaml
│   │   ├── compose.dev.yaml
│   │   └── compose.prod.yaml
│   ├── aws/
│   ├── terraform/
│   └── kubernetes/
├── scripts/
│   ├── backup.sh
│   ├── restore.sh
│   ├── deploy.sh
│   └── health-check.sh
├── docs/
│   ├── architecture.md
│   ├── api.md
│   ├── deployment.md
│   ├── troubleshooting.md
│   ├── security.md
│   ├── cost-safety.md
│   ├── adr/
│   └── learning-log.md
├── .github/
│   ├── workflows/
│   ├── pull_request_template.md
│   └── ISSUE_TEMPLATE/
├── .env.example
├── .gitignore
├── Makefile
├── README.md
└── LICENSE
```

ไม่ต้องสร้างโครงสร้างทั้งหมดตั้งแต่วันแรก ให้เพิ่มเฉพาะเมื่อบทเรียนต้องใช้

---

# 9. แผนหลักสูตรแบบ Step-by-Step

หลักสูตรแบ่งเป็น 14 Phase โดยใช้เวลาประมาณ 10–14 สัปดาห์ หากเรียนสัปดาห์ละ 6–8 ชั่วโมง แต่สามารถเรียนตามเวลาจริงของผู้เรียนได้

---

# Phase 0 — Baseline, Learning Contract และ Cost Safety

## เป้าหมาย

- ตรวจสภาพแวดล้อม
- กำหนดวิธีเรียน
- สร้างกฎด้านค่าใช้จ่ายและความปลอดภัย
- เก็บ Baseline ความรู้ก่อนเริ่ม

## Lesson 0.1 — Environment Audit

ให้ตรวจสอบ

```bash
git --version
docker --version
docker compose version
python --version
ssh -V
```

ตรวจระบบปฏิบัติการ, RAM, Disk และ Port ที่ใช้งาน

## Lesson 0.2 — Baseline Quiz

ให้ผู้เรียนอธิบายด้วยตนเอง

- Image ต่างจาก Container อย่างไร
- Port ภายในกับ Port ที่ Publish ต่างกันอย่างไร
- Volume มีไว้ทำอะไร
- `localhost` ใน Container หมายถึงอะไร
- Git Commit, Push และ Pull Request ต่างกันอย่างไร
- CI และ CD ต่างกันอย่างไร

ใช้คำตอบนี้เป็น Baseline ไม่ต้องคาดหวังให้ถูกทั้งหมด

## Lesson 0.3 — Cost Safety Policy

สร้าง `docs/cost-safety.md` โดยกำหนดว่า

- เรียน Local-first
- สร้าง AWS Resource เฉพาะในบทที่เกี่ยวข้อง
- ตั้ง Budget/Cost Alert ก่อนสร้าง Compute Resource
- Tag Resource ทุกตัวด้วย Project และ Owner
- ปิดหรือลบ Resource หลังจบบท
- ตรวจ Billing Dashboard ทุกครั้งหลัง Lab Cloud
- หลีกเลี่ยง Managed Service ราคาแพงในเส้นทางหลัก
- Kubernetes บน AWS เป็น Optional ไม่ใช่ Free-first
- ห้ามสร้าง NAT Gateway, EKS, RDS หรือ Load Balancer โดยไม่ศึกษา Cost ก่อน
- เก็บ Checklist การสร้างและทำลาย Resource

## Acceptance Criteria

- เครื่องพร้อมใช้งาน
- มี `docs/learning-log.md`
- มี `docs/cost-safety.md`
- ผู้เรียนอธิบาย Baseline ได้
- ยังไม่สร้าง AWS Resource

## Git Checkpoint

```text
chore: initialize learning documentation and cost safety policy
```

---

# Phase 1 — Git Workflow และ Repository Discipline

## เป้าหมาย

เข้าใจ Git เป็นระบบจัดการการเปลี่ยนแปลง ไม่ใช่แค่ที่เก็บไฟล์

## Lesson 1.1 — Repository Initialization

- สร้าง Repository
- สร้าง README ขั้นต้น
- สร้าง `.gitignore`
- สร้าง `.env.example`
- อธิบาย Working Tree, Staging Area และ Commit History

## Lesson 1.2 — Branch Workflow

ใช้แนวทาง Short-lived Feature Branch

```text
main
└── feature/bootstrap-api
```

ฝึก

- checkout/switch
- add
- commit
- diff
- log
- merge
- rebase ในระดับเบื้องต้น
- conflict แบบตั้งใจสร้าง

## Lesson 1.3 — Pull Request แบบทำคนเดียว

แม้ทำคนเดียว ให้เปิด Pull Request เพื่อฝึก

- Description
- Scope
- Test Evidence
- Risk
- Rollback

## Lesson 1.4 — Versioning

ใช้ Semantic Versioning แบบง่าย

```text
v0.1.0
v0.2.0
v1.0.0
```

อธิบาย Tag ต่างจาก Branch และ Commit อย่างไร

## Acceptance Criteria

- มี Repository ที่อ่านเข้าใจ
- มี Feature Branch อย่างน้อยหนึ่ง Branch
- มี Pull Request
- แก้ Conflict ได้
- อธิบาย Commit History ได้
- ไม่มี Secret ใน Repository

## Git Checkpoint

```text
chore: establish repository workflow and contribution rules
```

---

# Phase 2 — Backend แบบไม่ใช้ Docker ก่อน

## เป้าหมาย

เข้าใจ Application ก่อนซ่อนมันไว้ใน Container

## Lesson 2.1 — FastAPI Bootstrap

สร้าง API ขั้นต่ำ

```text
GET /health/live
GET /health/ready
```

อธิบาย

- Process
- Port
- Bind Address
- Request/Response
- HTTP Status Code
- Application Startup

## Lesson 2.2 — Configuration

ใช้ Environment Variable

```text
APP_ENV
APP_PORT
LOG_LEVEL
```

ห้าม Hardcode Secret

## Lesson 2.3 — Structured Logging

สร้าง Log ที่มี

- timestamp
- level
- service
- message
- request_id หากเหมาะสม

## Lesson 2.4 — Unit Test แรก

ทดสอบ Health Endpoint

เรียนรู้

- Arrange
- Act
- Assert
- Test Isolation
- Expected Failure

## Acceptance Criteria

- API รันบนเครื่องได้
- Health Endpoint ผ่าน
- Test ผ่าน
- Configuration อ่านจาก Environment
- ผู้เรียนอธิบายว่า Process ฟัง Port ได้อย่างไร

## Git Checkpoint

```text
feat(api): add application bootstrap and health endpoints
```

Tag:

```text
v0.1.0
```

---

# Phase 3 — Docker Fundamentals แบบหนึ่ง Container

## เป้าหมาย

เข้าใจว่า Container ทำอะไรและไม่ได้ทำอะไร

## Lesson 3.1 — Dockerfile ทีละบรรทัด

สร้าง Dockerfile โดยอธิบาย

- FROM
- WORKDIR
- COPY
- RUN
- ENV
- EXPOSE
- CMD
- Layer Cache

## Lesson 3.2 — Build Context และ `.dockerignore`

ทดลอง Build ช้าและ Build เร็วเพื่อเห็น Cache

## Lesson 3.3 — Container Lifecycle

ฝึก

```bash
docker build
docker run
docker ps
docker logs
docker exec
docker inspect
docker stop
docker rm
```

## Lesson 3.4 — Bind Address Problem

ทดลองให้ API Bind เฉพาะ `127.0.0.1` แล้วดูว่าเข้าจากภายนอก Container ไม่ได้ จากนั้นแก้เป็น `0.0.0.0`

## Lesson 3.5 — Non-root User และ Image Size

- รัน App ด้วย Non-root User
- เปรียบเทียบ Base Image
- ตรวจ Image Layers

## Acceptance Criteria

- Build Image สำเร็จ
- Container รันได้
- เข้าถึง API ผ่าน Published Port ได้
- อธิบาย `EXPOSE` กับ `-p` ได้
- อธิบาย Layer Cache ได้
- Container ไม่รันเป็น Root หากทำได้เหมาะสม

## Git Checkpoint

```text
build(api): containerize backend service
```

Tag:

```text
v0.2.0
```

---

# Phase 4 — PostgreSQL, Persistence และ Migration

## เป้าหมาย

เข้าใจข้อมูลถาวรและ Lifecycle ที่ต่างจาก Application Container

## Lesson 4.1 — Data Model

ตารางขั้นต่ำ

```text
devices
telemetry
```

กำหนด Primary Key, Unique Key, Foreign Key และ Index

## Lesson 4.2 — PostgreSQL Container

เพิ่ม Database ด้วย Docker Compose

เรียนรู้

- Service Name
- Internal DNS
- Container Port
- Host Port
- Environment
- Named Volume

## Lesson 4.3 — Connection String

อธิบายว่าทำไม Backend ต้องใช้ Host เป็น `db` ไม่ใช่ `localhost`

## Lesson 4.4 — Alembic Migration

- สร้าง Migration
- Upgrade
- Downgrade
- ตรวจ Schema
- ห้ามใช้ `create_all()` แทน Migration ใน Production Path

## Lesson 4.5 — Persistence Experiment

- เพิ่มข้อมูล
- ลบ Container แต่ไม่ลบ Volume
- สร้าง Container ใหม่
- ยืนยันว่าข้อมูลยังอยู่
- จากนั้นอธิบายความเสี่ยงของ `docker compose down -v`

## Lesson 4.6 — Readiness

แยก

- Liveness
- Readiness

Backend Ready เมื่อเชื่อม Database ได้

## Acceptance Criteria

- API เชื่อม PostgreSQL ผ่าน Compose Network
- Migration ใช้งานได้
- Volume รักษาข้อมูลได้
- Readiness สะท้อนสถานะ Database จริง
- ผู้เรียนอธิบาย Data Loss Scenario ได้

## Git Checkpoint

```text
feat(storage): add PostgreSQL persistence and database migrations
```

Tag:

```text
v0.3.0
```

---

# Phase 5 — Multi-Container Compose และ Service Dependency

## เป้าหมาย

เข้าใจการประกอบระบบหลาย Service

## Lesson 5.1 — Compose Specification

อ่านและอธิบายส่วนสำคัญ

- services
- networks
- volumes
- environment
- env_file
- depends_on
- healthcheck
- restart policy

## Lesson 5.2 — Health Check

เพิ่ม Health Check ให้ Database และ API

ทดลองทำ Database ไม่พร้อมแล้วดู Behavior

## Lesson 5.3 — Startup ไม่เท่ากับ Ready

อธิบายว่า `depends_on` ไม่ได้แก้ทุกปัญหา ต้องให้ Application Retry Connection อย่างเหมาะสม

## Lesson 5.4 — Compose Profiles/Overrides

แยก

```text
compose.yaml
compose.dev.yaml
compose.prod.yaml
```

โดยไม่ Duplicate Config เกินจำเป็น

## Lesson 5.5 — Resource Awareness

ตรวจ

```bash
docker stats
```

สังเกต CPU และ Memory ของแต่ละ Service

## Acceptance Criteria

- `docker compose up -d` ทำให้ Core Stack ทำงาน
- Health Status ถูกต้อง
- API Recover ได้เมื่อ Database กลับมา
- ผู้เรียนวาด Network Diagram ได้
- อธิบาย Startup Order และ Readiness ได้

## Git Checkpoint

```text
build(compose): orchestrate API and database services
```

---

# Phase 6 — MQTT Broker และ Device Simulator

## เป้าหมาย

เรียน Event-driven Communication และความแตกต่างจาก REST

## Lesson 6.1 — MQTT Concepts

อธิบาย

- Broker
- Publisher
- Subscriber
- Topic
- QoS
- Retained Message
- Clean Session
- At-most-once / At-least-once

## Lesson 6.2 — Mosquitto Container

เพิ่ม `broker`

กำหนด Config แบบ Development ก่อน แล้วค่อยเพิ่ม Authentication

## Lesson 6.3 — Simulator

สร้าง Simulator ที่

- มี Device ID
- ส่งข้อมูลทุกช่วงเวลา
- ตั้งค่า Interval ผ่าน Environment
- ปิดตัวอย่าง Graceful เมื่อได้รับ Signal
- มี Retry/Reconnect

## Lesson 6.4 — Backend Subscriber

Backend Subscribe Topic และ Validate Payload ด้วย Pydantic

## Lesson 6.5 — Idempotency และ Duplicate Message

จำลองส่งข้อมูลซ้ำ และออกแบบ Unique Constraint หรือ Message ID เพื่อไม่บันทึกซ้ำโดยไม่ตั้งใจ

## Lesson 6.6 — REST vs MQTT

ให้ผู้เรียนอธิบายว่า

- เมื่อไรควรใช้ REST
- เมื่อไรควรใช้ MQTT
- ต่างกันด้าน Coupling, Retry และ Delivery อย่างไร

## Acceptance Criteria

- Simulator ส่งข้อมูล
- Broker รับข้อมูล
- Backend บันทึกลง Database
- Payload ผิด Schema ถูกปฏิเสธและมี Log
- Reconnect ทำงาน
- ผู้เรียนอธิบาย QoS และ Duplicate ได้

## Git Checkpoint

```text
feat(telemetry): ingest simulated device data through MQTT
```

Tag:

```text
v0.4.0
```

---

# Phase 7 — REST API, Frontend และ Reverse Proxy

## เป้าหมาย

ทำให้ระบบใช้งานจาก Browser ผ่าน Entry Point เดียว

## Lesson 7.1 — Query API

สร้าง

- Device List
- Latest Telemetry
- Telemetry History
- Pagination
- Time Range Filter

## Lesson 7.2 — Minimal Frontend

สร้าง Dashboard เบา ๆ ที่

- แสดงรายการ Device
- แสดงค่าล่าสุด
- แสดงประวัติแบบตารางหรือกราฟง่าย
- แสดง Error State
- ไม่ซ่อน API Error

Frontend ไม่ใช่เป้าหมายหลัก จึงไม่ต้องซับซ้อน

## Lesson 7.3 — NGINX Reverse Proxy

Route ตัวอย่าง

```text
/       → frontend
/api/   → api
```

อธิบาย

- Reverse Proxy
- Upstream
- Forwarded Headers
- Timeout
- Request Size
- Static File Caching

## Lesson 7.4 — CORS Before and After Proxy

ทดลองเรียก API ต่าง Origin และอธิบายว่า Proxy ช่วยลดความซับซ้อนได้อย่างไร

## Lesson 7.5 — Basic Security Headers

เพิ่ม Header ที่เหมาะสมโดยไม่ Copy แบบไม่เข้าใจ

## Lesson 7.6 — Local Self-Signed HTTPS

สร้าง Self-Signed Certificate สำหรับ Local Lab แล้วกำหนดให้ NGINX ทำ TLS Termination

```text
Browser → HTTPS :443 → NGINX → HTTP ภายใน Docker Network → Backend
```

ฝึกและอธิบาย

- Certificate และ Private Key
- Browser Trust Warning
- Port 443
- TLS Termination
- HTTP to HTTPS Redirect
- Certificate Expiration
- ห้าม Commit Private Key ลง Git

## Acceptance Criteria

- Browser เข้า Entry Point เดียว
- Frontend เรียก API ผ่าน Proxy
- ไม่มีการ Hardcode `localhost` ที่ผิดบริบท
- API Error แสดงผลเหมาะสม
- ผู้เรียนอธิบาย Reverse Proxy และ CORS ได้
- เข้า Local NGINX ผ่าน Self-Signed HTTPS ได้
- อธิบายว่า Encryption ต่างจาก Public Trust อย่างไรได้
- Private Key ไม่อยู่ใน Repository

## Git Checkpoint

```text
feat(web): add dashboard and NGINX reverse proxy
```

Tag:

```text
v0.5.0
```

---

# Phase 8 — Testing, Code Quality และ Security Scan

## เป้าหมาย

สร้างความมั่นใจก่อน Build และ Deploy

## Lesson 8.1 — Testing Pyramid

แบ่ง

- Unit Test
- Integration Test
- End-to-End Test

อธิบายข้อดีและต้นทุนของแต่ละระดับ

## Lesson 8.2 — Database Integration Test

ใช้ Database แยกสำหรับ Test และล้างข้อมูลอย่างปลอดภัย

## Lesson 8.3 — MQTT Integration Test

Publish Test Message แล้วตรวจ Record ใน Database

## Lesson 8.4 — Lint and Format

ใช้ Ruff และตรวจใน CI ภายหลัง

## Lesson 8.5 — Type Checking

ใช้ MyPy เฉพาะจุดที่ให้ประโยชน์ ไม่ต้องทำให้ซับซ้อนเกินไป

## Lesson 8.6 — Dependency and Container Scan

ใช้เครื่องมือ เช่น Trivy เพื่อให้เห็น Vulnerability และเรียนรู้ว่า

- ไม่ใช่ทุก Warning ต้องแก้แบบเดียวกัน
- ต้องดู Severity
- ต้องดู Exploitability
- ต้องดู Base Image และ Package Version

## Acceptance Criteria

- Unit Test ผ่าน
- Integration Test ผ่าน
- Lint ผ่าน
- Scan ทำงานและผู้เรียนอ่านผลได้
- มีคำสั่งเดียวสำหรับตรวจคุณภาพ เช่น `make check`

## Git Checkpoint

```text
test: add automated quality and integration checks
```

Tag:

```text
v0.6.0
```

---

# Phase 9 — Continuous Integration ด้วย GitHub Actions

## เป้าหมาย

ทุก Push/Pull Request ต้องถูกตรวจสอบอัตโนมัติ

## Lesson 9.1 — CI Workflow แรก

Trigger

```text
pull_request
push to main
```

Jobs ขั้นต่ำ

1. Checkout
2. Set up Python
3. Install Dependencies
4. Lint
5. Unit Test

## Lesson 9.2 — Service Container หรือ Compose Test

เพิ่ม PostgreSQL สำหรับ Integration Test

## Lesson 9.3 — Cache

เรียน Dependency Cache และข้อดี/ความเสี่ยงของ Cache เก่า

## Lesson 9.4 — Build Docker Image

CI ต้อง Build Image ได้ แต่ยังไม่ Push

## Lesson 9.5 — Security Scan

Scan Image หลัง Build

## Lesson 9.6 — Branch Protection

หากบัญชีรองรับ ให้กำหนดว่า Merge ได้เมื่อ CI ผ่าน

## Acceptance Criteria

- Pull Request แสดง CI Status
- CI Fail เมื่อ Test Fail
- CI Fail เมื่อ Lint Fail
- Docker Build ผ่าน
- Scan ทำงาน
- ผู้เรียนอธิบาย Runner, Job, Step และ Artifact ได้

## Git Checkpoint

```text
ci: validate code and container builds on every pull request
```

Tag:

```text
v0.7.0
```

---

# Phase 10 — Container Registry และ Release Management

## เป้าหมาย

สร้าง Artifact ที่ Deploy ซ้ำได้และระบุ Version ชัดเจน

## Lesson 10.1 — Image Naming

ตัวอย่าง

```text
ghcr.io/<owner>/mini-telemetry-api
```

## Lesson 10.2 — Tag Strategy

ใช้

```text
sha-<short_commit>
v0.8.0
latest
```

อธิบายว่าทำไม Production ไม่ควรพึ่ง `latest` เพียงอย่างเดียว

## Lesson 10.3 — Registry Authentication

ใช้ GitHub Token/Secrets อย่างปลอดภัย

## Lesson 10.4 — Release Workflow

เมื่อ Tag Version

- Test
- Build
- Scan
- Push Image
- สร้าง Release Notes ขั้นต้น

## Lesson 10.5 — Reproducibility

พิสูจน์ว่าเครื่องอื่นสามารถ Pull Image แล้วรันได้โดยไม่ใช้ Source Code Local

## Acceptance Criteria

- Registry มี Versioned Image
- Image เชื่อมโยงกลับไปยัง Commit ได้
- ไม่มี Password ใน Workflow
- Pull และ Run Image บนเครื่องใหม่ได้
- ผู้เรียนอธิบาย Artifact และ Immutability ได้

## Git Checkpoint

```text
ci(release): publish versioned container images
```

Tag:

```text
v0.8.0
```

---

# Phase 11 — Cloud Foundation แบบ Free-tier Gated

## เป้าหมาย

เข้าใจ Cloud Infrastructure และทำ Hands-on โดยรักษาค่าใช้จ่ายจริงที่ 0 บาท

## ข้อบังคับก่อนเริ่ม

ก่อนแตะ AWS ต้องทำ `docs/aws-free-tier-gate.md` ให้ครบ หากข้อใดไม่ผ่าน ห้ามสร้าง Resource และใช้ Local Simulation Track

AWS Track ห้าม

- Upgrade เป็น Paid plan
- เข้าร่วม AWS Organizations
- ใช้ NAT Gateway, RDS, EKS, Load Balancer, Marketplace หรือ Paid-only Feature
- เปิด Resource ทิ้งหลังจบ Session
- เชื่อว่า Budget Alert เป็น Hard Limit

## Lesson 11.1 — Cloud Mental Model

อธิบาย

- Region
- Availability Zone
- VPC
- Subnet
- Route
- Internet Gateway
- Security Group
- EC2
- Public/Private IP
- IAM

## Lesson 11.2 — IAM และ Account Safety

- เปิด MFA สำหรับ Root หากใช้ AWS Track
- ไม่ใช้ Root ทำงานประจำ
- เปรียบเทียบ Root, User และ Role
- ออกแบบ Least Privilege Policy
- อธิบาย Access Key, Console Login และ MFA
- ห้ามใส่ Secret จริงใน Lab

## Lesson 11.3 — Deployment Target: Local ก่อน AWS

เริ่มด้วย Linux Container หรือ Local VM แล้วจึงทำ EC2 ขนาดเล็กเมื่อ Free-tier Gate ผ่าน

- Linux environment
- User/permission
- Docker network และ published port
- ตรวจ Disk, RAM และ Network
- บันทึก Mapping ว่าส่วนใดเทียบได้กับ EC2 และส่วนใดเทียบไม่ได้
- หากทำ AWS Track ให้บันทึก Instance Type, Storage, Public IPv4, Region, Credit ก่อน/หลัง และเวลาที่ต้อง Terminate

ยังไม่ใช้ Terraform เพื่อให้เห็น Deployment Target และ Network จริงก่อน

## Lesson 11.4 — Port Exposure และ Security Group

ทดลอง

- ไม่ Publish Port แล้วเข้าถึงจาก Host ไม่ได้
- Publish เฉพาะ Port ที่จำเป็นบน `127.0.0.1`
- ห้ามเปิด PostgreSQL และ MQTT สู่ Public Network
- หากทำ EC2 Lab ให้เปิด HTTP Port 80 ชั่วคราวกับข้อมูลจำลอง
- SSH Port 22 ต้องจำกัด Source เป็น IP ของผู้เรียน ห้ามเปิด `0.0.0.0/0`
- ห้ามส่ง Password, Token, Cookie หรือข้อมูลส่วนบุคคลผ่าน Public HTTP

## Lesson 11.5 — Zero-cost and Destroy Drill

หลังจบ Lab

- Stop/Remove Local Resource ตามแผนโดยไม่ลบข้อมูลสำคัญ
- ตรวจ Container, Network, Volume และ Process ค้าง
- AWS Track ต้อง Terminate EC2 และลบ Volume, Snapshot และ Elastic/Public IP ที่ไม่ใช้
- ตรวจทุก Region, Billing, Credit Balance และรายการ Resource ที่เกี่ยวข้อง
- ยืนยันค่าใช้จ่ายจริง 0 บาทและบันทึกหลักฐานใน Learning Log

## Acceptance Criteria

- Local Simulation ผ่านเสมอ ไม่ว่าบัญชี AWS จะมีสถานะใด
- มี `docs/aws-free-tier-gate.md` พร้อมผล PASS หรือ LOCAL-ONLY
- มี Cloud Architecture Diagram และ IAM Policy ตัวอย่าง
- เข้า Local Linux Deployment Target ได้
- Published Port เปิดเท่าที่จำเป็นและผูกกับ `127.0.0.1` เมื่อเหมาะสม
- อธิบาย VPC/Subnet/Security Group ระดับพื้นฐานได้
- ทำ Local Cleanup Checklist ได้
- อธิบายข้อจำกัดของ Local Simulation เมื่อเทียบกับ AWS ได้
- หาก Gate ผ่าน: Deploy EC2 Lab, ตรวจ Billing และ Destroy Resource ได้โดยค่าใช้จ่ายจริง 0 บาท

## Git Checkpoint

```text
docs(cloud): document free-tier gate and zero-cost cloud lab
```

---

# Phase 12 — Continuous Delivery แบบ Local-first และ AWS Credit-gated

## เป้าหมาย

เปลี่ยนจาก Deploy ด้วยมือเป็นกระบวนการที่ควบคุมได้ โดยต้องผ่าน Local ก่อนและใช้ AWS เฉพาะเมื่อ Free-tier Gate ยังผ่าน

## Lesson 12.1 — Manual Production Deployment

ก่อนทำ Auto Deploy ให้ Deploy ด้วยมือหนึ่งครั้ง

```text
Pull versioned images
Load environment file
docker compose up -d
Run health check
```

อธิบายทุกขั้นตอน

## Lesson 12.2 — Production Compose

สร้าง Production Override

- ไม่ Mount Source Code
- ใช้ Versioned Image
- Restart Policy
- Resource Limits หากเหมาะสม
- Log Rotation
- Health Check
- Secret จาก Server Environment

## Lesson 12.3 — Deployment Script

สร้าง Script ที่

- ตรวจ Environment
- Pull Image
- บันทึก Version ปัจจุบัน
- Deploy
- รอ Health Check
- Fail อย่างชัดเจน
- ไม่ลบข้อมูล

## Lesson 12.4 — Local CD และ Optional AWS CD

เริ่มด้วย Manual Approval และ Deployment Script บนเครื่อง Local เมื่อผ่านแล้วจึงเปลี่ยน Target เป็น EC2 เฉพาะ Credit-gated Lab

Pipeline

```text
Release Tag
→ CI Passed
→ Build/Push Image
→ Select Local Deployment Target
→ Pull Image
→ Compose Up
→ Health Check
→ Report Result
```

AWS Target ต้องมี Final Manual Approval, Credit Check ก่อน Deploy และ Destroy Step/Runbook หลังจบ Lab

## Lesson 12.5 — Secret Management

- Environment Variable/Secret สำหรับ Local Lab
- Server `.env`
- SSH Private Key
- Known Hosts
- ห้าม Print Secret ใน Log

## Lesson 12.6 — Rollback

หาก Health Check Fail

- กลับไป Image Tag ก่อนหน้า
- รัน Compose อีกครั้ง
- ยืนยัน Health

## Acceptance Criteria

- Deploy Version ใหม่ได้
- Pipeline ไม่ใช้ `latest` อย่างเดียว
- Secret ไม่รั่ว
- Health Check หลัง Deploy ทำงาน
- Rollback ได้
- ผู้เรียนอธิบาย Continuous Delivery กับ Continuous Deployment ได้
- Local Track เพียงพอต่อการผ่าน; AWS Track ต้องไม่เกิดค่าใช้จ่ายจริงและไม่มี Resource ค้าง

## Git Checkpoint

```text
cd: deploy locally and validate optional free-tier target
```

Tag:

```text
v0.9.0
```

---

# Phase 13 — Observability, Backup และ Incident Practice

## เป้าหมาย

เรียนรู้ว่าการ Deploy สำเร็จยังไม่ถือว่าระบบดูแลได้

## Lesson 13.1 — Three Pillars

อธิบาย

- Logs
- Metrics
- Traces

หลักสูตรนี้เน้น Logs และ Metrics ก่อน

## Lesson 13.2 — Application Metrics

เพิ่ม Metrics เช่น

- Request Count
- Error Count
- Request Duration
- MQTT Messages Received
- Invalid Payload Count
- Database Insert Failure

## Lesson 13.3 — Local Monitoring Stack

เพิ่ม Prometheus/Grafana ใน Local Profile ก่อน

ไม่บังคับนำทุกตัวขึ้น EC2 เครื่องเล็ก

## Lesson 13.4 — Log Management

- Container Log
- Application Log
- Log Rotation
- Correlation/Request ID
- หลีกเลี่ยง Log Secret และ Personal Data

## Lesson 13.5 — Database Backup

สร้าง Backup Script

- Timestamped File
- Exit Code
- Retention
- Verify File
- ห้ามถือว่า Backup สำเร็จเพียงเพราะมีไฟล์

## Lesson 13.6 — Restore Drill

สร้าง Database ใหม่แล้ว Restore เพื่อพิสูจน์ว่า Backup ใช้ได้จริง

## Lesson 13.7 — Incident Simulation

ให้ Codex เลือกทำให้พังทีละเหตุการณ์ เช่น

- Database หยุด
- Broker หยุด
- Disk เต็มจำลอง
- Environment ผิด
- Image Tag ไม่มี
- Migration ไม่ตรง
- Security Group ปิด Port
- Health Check Fail

ผู้เรียนต้องใช้ Runbook วิเคราะห์

## Acceptance Criteria

- มี Dashboard/Metric ขั้นพื้นฐานใน Local
- Log อ่านและค้นหาได้
- Backup สำเร็จ
- Restore สำเร็จ
- มี Incident Report อย่างน้อยหนึ่งฉบับ
- ผู้เรียนอธิบาย Root Cause และ Prevention ได้

## Git Checkpoint

```text
ops: add monitoring, backup, restore and incident runbooks
```

Tag:

```text
v1.0.0
```

---

# Phase 14 — Kubernetes แบบ Local-first และ Infrastructure as Code

## เป้าหมาย

เชื่อมความเข้าใจจาก Docker Compose ไป Kubernetes โดยไม่เสียค่าใช้จ่าย Cloud โดยไม่จำเป็น

## Part A — Kubernetes Local

### Lesson 14.1 — Concept Mapping

เปรียบเทียบ

| Docker Compose | Kubernetes |
|---|---|
| Service | Deployment/StatefulSet + Service |
| Container | Container ใน Pod |
| Compose Network DNS | Kubernetes Service DNS |
| Environment | ConfigMap/Secret |
| Volume | PersistentVolume/PersistentVolumeClaim |
| Restart Policy | Controller Reconciliation |
| Scale | Replica Count/HPA |

### Lesson 14.2 — Pod และ Deployment

Deploy API แบบหนึ่ง Replica ก่อน

### Lesson 14.3 — Service Discovery

ให้ API คุยกับ Database ผ่าน Service Name

### Lesson 14.4 — ConfigMap และ Secret

อธิบายว่า Kubernetes Secret ไม่ได้เข้ารหัสโดยอัตโนมัติในทุกบริบท

### Lesson 14.5 — Readiness/Liveness Probe

นำ Health Endpoint ที่สร้างไว้กลับมาใช้

### Lesson 14.6 — Scaling

เพิ่ม API Replica และสังเกต

- Request Distribution
- Stateless Requirement
- Database Shared State

### Lesson 14.7 — Rolling Update/Rollback

Deploy Image Version ใหม่ และ Rollback

### Lesson 14.8 — Persistent Data

อธิบายว่าทำไม Database บน Kubernetes ซับซ้อนกว่า API และไม่ควรย้ายแบบไม่เข้าใจ

## Part B — Terraform

### Lesson 14.9 — Infrastructure as Code Concepts

อธิบาย

- Declarative
- State
- Plan
- Apply
- Destroy
- Drift
- Idempotency

### Lesson 14.10 — Local Resource และ Optional AWS Definition

เขียน Terraform สำหรับ Local Resource ก่อน จากนั้นเขียน AWS Definition ได้เมื่อ Free-tier Gate ผ่าน โดยห้าม Apply หาก Gate ไม่ผ่าน

ต้อง `terraform plan` และอ่านผลก่อน `apply`

### Lesson 14.11 — Destroy Drill

ใช้ `terraform destroy` แล้วตรวจ State และเครื่อง Local หากทำ AWS Track ต้องตรวจ Console ทุก Region ว่าไม่มี Resource ค้าง

## Acceptance Criteria

- Deploy API บน Local Kubernetes ได้
- Scale Replica ได้
- Probe ทำงาน
- Rolling Update และ Rollback ได้
- อธิบาย Pod ต่างจาก Container ได้
- Terraform Plan/Apply/Destroy กับ Local Resource ได้
- อธิบาย State และ Drift ได้
- ไม่จำเป็นต้องสร้าง EKS ใน Free-first Track

## Git Checkpoint

```text
feat(platform): add local Kubernetes and infrastructure-as-code labs
```

Tag:

```text
v1.1.0
```

---

# 10. Capstone Exam

Codex ต้องจัดสอบปลายหลักสูตรโดยไม่แก้ให้ทันที

## Scenario

ให้เครื่องหรือ Environment ใหม่ ผู้เรียนต้องทำต่อไปนี้

1. Clone Repository
2. ตั้งค่า `.env`
3. รัน Test
4. Build Image
5. Start Local Stack
6. ตรวจ Health
7. ส่ง MQTT Message
8. ตรวจ Database
9. เรียก REST API
10. เปิด Dashboard
11. ทำให้ Service หนึ่งพัง
12. วิเคราะห์และกู้คืน
13. สร้าง Release Tag
14. ให้ CI ทำงาน
15. Deploy Version ใหม่
16. Rollback
17. Backup
18. Restore
19. วาด Architecture
20. อธิบาย Security และ Cost Risks

## Oral Questions

- ทำไม API Container จึงใช้ `db` แทน `localhost`
- ถ้าลบ Container Database ข้อมูลหายหรือไม่ เพราะอะไร
- ถ้าลบ Volume เกิดอะไรขึ้น
- Health Check แบบ Live และ Ready ต่างกันอย่างไร
- CI ตรวจอะไร และ CD ทำอะไร
- ทำไมไม่ใช้ `latest` เป็น Production Version เพียง Tag เดียว
- Secret ควรอยู่ที่ไหน
- Security Group ต่างจาก Firewall ในเครื่องอย่างไร
- Reverse Proxy มีประโยชน์อะไร
- MQTT ต่างจาก REST อย่างไร
- Kubernetes Scale อะไร
- Gunicorn Scale อะไร
- Serverless Function Scale อะไร
- เมื่อไร Docker Compose เพียงพอ
- เมื่อไร Kubernetes เริ่มมีประโยชน์
- Backup ที่ไม่เคย Restore ถือว่าเชื่อถือได้หรือไม่
- ถ้า Deploy ผ่านแต่ User ใช้งานไม่ได้ จะตรวจจากจุดไหนก่อน

## เกณฑ์ผ่าน

ผู้เรียนต้อง

- ทำระบบทำงานได้
- อธิบายเหตุผลของ Config สำคัญได้
- แก้ปัญหาโดยใช้ Log และคำสั่งตรวจสอบ
- ไม่พึ่งการลบทุกอย่างแล้วสร้างใหม่
- ไม่เปิด Port เกินจำเป็น
- ไม่ Commit Secret
- ทำ Rollback และ Restore ได้
- อธิบาย Architecture ได้ด้วยคำของตนเอง

---

# 11. เอกสารที่ต้องมีเมื่อจบ

```text
README.md
docs/architecture.md
docs/api.md
docs/deployment.md
docs/troubleshooting.md
docs/security.md
docs/cost-safety.md
docs/backup-restore.md
docs/incident-report.md
docs/learning-log.md
docs/adr/
```

## Architecture Decision Record ที่ควรมี

- ADR-001: เลือก FastAPI
- ADR-002: เลือก PostgreSQL
- ADR-003: เลือก MQTT สำหรับ Telemetry
- ADR-004: ใช้ Docker Compose สำหรับ Single-host Deployment
- ADR-005: ใช้ Versioned Container Image
- ADR-006: ใช้ Local Kubernetes แทน EKS ใน Free-first Track
- ADR-007: แนวทาง Secret Management
- ADR-008: Backup and Restore Strategy

---

# 12. Definition of Done ของแต่ละ Feature

Feature ถือว่าเสร็จเมื่อ

- Code ทำงาน
- Test ผ่าน
- Lint ผ่าน
- Log เพียงพอ
- Error Handling เหมาะสม
- Config ไม่ Hardcode
- Secret ไม่อยู่ใน Git
- Documentation อัปเดต
- Health Check ไม่ได้รับผลกระทบ
- Docker Build ผ่าน
- ผู้เรียนอธิบายได้
- มี Git Commit ที่ชัดเจน

---

# 13. Debugging Framework ที่ต้องใช้ตลอดหลักสูตร

ใช้ลำดับ **O-H-T-F**

## Observe

- อาการจริงคืออะไร
- Expected คืออะไร
- เกิดเมื่อไร
- Service ใดเกี่ยวข้อง
- มี Log อะไร

## Hypothesize

ตั้งสมมติฐาน 2–3 ข้อก่อนแก้

## Test

ใช้คำสั่งหรือการทดลองที่เปลี่ยนตัวแปรทีละอย่าง

## Fix and Verify

- แก้สาเหตุ
- ทดสอบซ้ำ
- ตรวจ Regression
- บันทึก Root Cause
- เพิ่ม Test หรือ Monitoring ป้องกันการเกิดซ้ำ

คำสั่งที่ควรฝึกใช้ เช่น

```bash
docker compose ps
docker compose logs
docker inspect
docker stats
curl
ss
ip
ping
nslookup
dig
ps
top
free
df
journalctl
psql
```

Codex ต้องอธิบายว่าคำสั่งแต่ละตัวตรวจ Layer ใดของระบบ

---

# 14. แนวทางจัดเวลา

## รูปแบบแนะนำต่อหนึ่ง Session

- 15 นาที: ทบทวนบทก่อน
- 20 นาที: แนวคิดใหม่
- 60–90 นาที: Lab
- 20 นาที: Debug/Experiment
- 15 นาที: Quiz
- 10 นาที: Git Commit และ Learning Log

## ห้ามรีบ

หากบทใดไม่เข้าใจ ให้ทำซ้ำด้วยการ

- วาด Diagram
- อธิบายด้วยภาษาง่าย
- ทำ Experiment เพิ่ม
- ลบเฉพาะ Component ที่ปลอดภัยแล้วสร้างใหม่
- เปรียบเทียบ Behavior ก่อนและหลัง

---

# 15. Milestone Summary

| Milestone | ผลลัพธ์ |
|---|---|
| M1 | API รัน Local และมี Test |
| M2 | API รันใน Docker |
| M3 | API + PostgreSQL ใน Compose |
| M4 | MQTT + Simulator + Persistence |
| M5 | Frontend + NGINX |
| M6 | Test/Lint/Scan ครบ |
| M7 | GitHub Actions CI |
| M8 | Versioned Image ใน Registry |
| M9 | Free-tier Gate + Local Cloud Simulation + Optional EC2 Lab ราคา 0 บาท |
| M10 | Local CD + Optional AWS CD + Health Check + Rollback |
| M11 | Monitoring + Backup/Restore |
| M12 | Local Kubernetes + Terraform |
| Final | Capstone ผ่านและอธิบายระบบได้ทั้งหมด |

---

# 16. คำสั่งเริ่มต้นที่ Codex ต้องทำเมื่อได้รับเอกสารนี้

เมื่อเริ่มหลักสูตร ห้ามสร้างโปรเจกต์ทั้งหมดทันที ให้ทำตามลำดับนี้

1. สรุปความเข้าใจต่อเป้าหมายของผู้เรียนไม่เกิน 10 ข้อ
2. ตรวจสอบว่าขณะนี้อยู่ใน Repository ใด
3. ตรวจไฟล์ที่มีอยู่ก่อน
4. ตรวจ Environment ด้วยคำสั่งพื้นฐาน
5. ทำ Baseline Quiz
6. สร้างเฉพาะไฟล์เริ่มต้นของ Phase 0
7. อธิบาย Diff ทุกไฟล์
8. ให้ผู้เรียนตรวจและ Commit
9. รอการยืนยันก่อนเริ่ม Phase 1

ข้อความเปิดบทเรียนที่ควรใช้:

> เราจะสร้าง Mini Telemetry Platform แบบ Production-minded แต่ Free-first โดยจะเพิ่มความซับซ้อนทีละขั้น ผมจะไม่สร้างระบบทั้งหมดให้ทันที ทุกบทจะมีแนวคิด Lab การตรวจผล คำถาม และ Acceptance Criteria คุณสามารถใช้ AI ช่วยได้ แต่ก่อนผ่านแต่ละบท คุณต้องอธิบายส่วนสำคัญด้วยคำของคุณเอง

---

# 17. หลักการตัดสินใจเมื่อมีหลายทางเลือก

Codex ต้องเสนออย่างน้อย

- ทางเลือกที่ง่ายที่สุด
- ทางเลือกที่เหมาะกับ Production มากขึ้น
- Trade-off
- ค่าใช้จ่าย
- ความซับซ้อน
- สิ่งที่ผู้เรียนจะได้เรียนรู้

จากนั้นให้ผู้เรียนเป็นคนเลือก เว้นแต่เป็นเรื่อง Security หรือ Data Loss ที่ต้องเตือนอย่างชัดเจน

---

# 18. เส้นทางหลักและเส้นทางเสริม

## เส้นทางหลักที่ต้องจบ

- Git
- FastAPI
- PostgreSQL
- Docker
- Docker Compose
- MQTT
- NGINX
- Test
- GitHub Actions
- Container Registry
- AWS EC2 แบบ Credit-gated หรือ Local Cloud Simulation
- CI/CD
- Monitoring
- Backup/Restore
- Local Kubernetes

## เส้นทางเสริมเมื่อมีเวลา

- Redis
- RabbitMQ
- OpenTelemetry
- Loki
- Terraform Module
- Ansible
- Blue/Green Deployment
- Canary Deployment
- S3 Backup
- CloudWatch Agent
- GitOps/Argo CD
- Serverless/Lambda
- Kubernetes บน Managed Cloud

ห้ามนำเส้นทางเสริมมาทำให้เส้นทางหลักซับซ้อนเกินจำเป็น

---

# 19. ผลงาน Portfolio เมื่อจบ

Repository ต้องทำให้ Recruiter หรือ Engineer คนอื่นเห็นว่า ผู้เรียนสามารถ

- ออกแบบระบบหลาย Service
- เขียน Backend และ Integration
- ใช้ Docker/Compose
- สร้าง CI/CD
- Deploy แบบ Production-minded บน Local และ Deploy Cloud เมื่อ Free-tier Gate ผ่าน
- ควบคุม Security และ Cost
- ทำ Monitoring
- ทำ Backup/Restore
- ใช้ Kubernetes เบื้องต้น
- เขียนเอกสาร Technical Writing

README ต้องมี

- Project Overview
- Architecture Diagram
- Data Flow
- Local Setup
- Test Instructions
- CI/CD Overview
- Deployment Guide
- Screenshots
- Security Considerations
- Cost Safety
- Known Limitations
- Future Improvements

---

# 20. คำเตือนสำคัญ

- หลักสูตรนี้วัดความเข้าใจ ไม่ใช่จำนวน Technology
- ไม่จำเป็นต้องใช้ Kubernetes บน AWS เพื่อพิสูจน์ว่าเข้าใจ Kubernetes
- ไม่จำเป็นต้องใช้ Managed Database เพื่อเรียน Database Production Concepts
- ไม่ควรเพิ่ม Microservice หากยังไม่มีเหตุผลด้าน Responsibility หรือ Scaling
- หลาย Container ไม่ได้แปลว่า Microservices ที่ดีโดยอัตโนมัติ
- CI/CD ที่ดีต้องตรวจสอบได้ Rollback ได้ และไม่ทำลายข้อมูล
- Cloud Resource ทุกตัวต้องมี Owner, Purpose และ Destroy Plan
- Backup ต้องผ่านการ Restore Test
- Monitoring ต้องตอบได้ว่า “เกิดอะไรขึ้น ที่ไหน และตั้งแต่เมื่อไร”
- AI ช่วยเร่งการเรียนได้ แต่ห้ามแทนที่การคิดและการตัดสินใจของผู้เรียน

---

# End of Course Instruction

Codex ต้องใช้เอกสารนี้เป็น Course Contract ตลอดโปรเจกต์ หากผู้เรียนขอให้ข้ามบท ให้เตือนผลกระทบและเสนอ Quick Review ก่อน หากมีการเปลี่ยน Architecture ให้บันทึกเป็น ADR และอัปเดต Diagram ทุกครั้ง
