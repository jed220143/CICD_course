# Checklist การเรียน Cloud, CI/CD และ Container Infrastructure

ไฟล์นี้ใช้ติดตามการเรียนจากแผน [CODEX_CLOUD_CICD_COURSE_PLAN_TH.md](./CODEX_CLOUD_CICD_COURSE_PLAN_TH.md) โดยยึดโปรเจกต์ **Mini Telemetry Platform** เป็นแกนหลัก

> หลักการสำคัญ: อย่าติ๊กงานว่าเสร็จเพียงเพราะคำสั่งรันผ่าน ให้ติ๊กเมื่อทำได้ อธิบายได้ และมีหลักฐานตรวจสอบได้ตาม Acceptance Criteria

## วิธีใช้

- ใช้ `[ ]` = ยังไม่เริ่ม, `[-]` = กำลังทำ/ยังไม่ผ่านครบ, `[x]` = ผ่านแล้ว
- กรอกวันที่ในรูปแบบ `YYYY-MM-DD`
- ทุก Phase ต้องมีหลักฐาน เช่น commit, PR, log, screenshot, test result, diagram หรือเอกสาร
- บันทึกสิ่งที่เข้าใจ สิ่งที่ยังสงสัย และปัญหาที่พบใน `docs/learning-log.md`
- ก่อนเริ่ม Phase ถัดไป ต้องผ่าน Acceptance Criteria ของ Phase ปัจจุบันครบ
- หากเปลี่ยน Architecture ให้สร้าง ADR และอัปเดต Diagram

## ข้อมูลผู้เรียน

| รายการ | ข้อมูล |
|---|---|
| ชื่อผู้เรียน |  |
| วันที่เริ่ม |  |
| เป้าหมายวันที่จบ |  |
| Repository |  |
| เวลาที่เรียนต่อสัปดาห์ |  |
| หมายเหตุ |  |

## สถานะรวม

| Phase | หัวข้อ | Milestone | สถานะ | วันที่ผ่าน |
|---:|---|---|---|---|
| 0 | Baseline, Learning Contract และ Cost Safety | เตรียมความพร้อม | [x] | 2026-07-13 |
| 1 | Git Workflow และ Repository Discipline | เตรียม Repository | [-] |  |
| 2 | Backend แบบไม่ใช้ Docker | M1 | [ ] |  |
| 3 | Docker Fundamentals | M2 | [ ] |  |
| 4 | PostgreSQL, Persistence และ Migration | M3 (ส่วนข้อมูล) | [ ] |  |
| 5 | Multi-Container Compose | M3 | [ ] |  |
| 6 | MQTT Broker และ Device Simulator | M4 | [ ] |  |
| 7 | REST API, Frontend และ Reverse Proxy | M5 | [ ] |  |
| 8 | Testing, Code Quality และ Security Scan | M6 | [ ] |  |
| 9 | Continuous Integration | M7 | [ ] |  |
| 10 | Container Registry และ Release Management | M8 | [ ] |  |
| 11 | Cloud Foundation แบบ Free-tier Gated | M9 | [ ] |  |
| 12 | Local-first CD + Optional AWS | M10 | [ ] |  |
| 13 | Observability, Backup และ Incident Practice | M11 | [ ] |  |
| 14 | Local Kubernetes และ Infrastructure as Code | M12 | [ ] |  |
| Final | Capstone Exam และ Portfolio | Final | [ ] |  |

---

## Phase 0 — Baseline, Learning Contract และ Cost Safety

### บทเรียนและงานลงมือทำ

- [x] Lesson 0.1 ตรวจ Environment และบันทึกเวอร์ชันเครื่องมือ
- [x] Lesson 0.2 ทำ Baseline Quiz และบันทึกหัวข้อที่ต้องทบทวน
- [x] Lesson 0.3 ตรวจและยอมรับนโยบาย Free-guaranteed/Credit-gated ฉบับปรับปรุง
- [x] สร้าง `docs/learning-log.md`
- [x] สร้าง `docs/cost-safety.md`
- [x] ยืนยันว่าจะยังไม่สร้าง AWS Resource ใน Phase นี้

### เกณฑ์ผ่าน

- [x] เครื่องพร้อมใช้งาน
- [x] มี `docs/learning-log.md`
- [x] มี `docs/cost-safety.md` และ `docs/aws-free-tier-gate.md`
- [x] อธิบาย Baseline ของตนเองได้
- [x] ยังไม่มี AWS Resource ที่สร้างจากหลักสูตร

**หลักฐาน/ลิงก์:**  
**สิ่งที่ยังสงสัย:**  
**วันที่ผ่าน:**  

---

## Phase 1 — Git Workflow และ Repository Discipline

### บทเรียนและงานลงมือทำ

- [x] Lesson 1.1 เริ่ม Repository และจัดโครงสร้างให้อ่านเข้าใจ
- [ ] Lesson 1.2 ฝึก Branch Workflow และแก้ Merge Conflict
- [ ] Lesson 1.3 สร้าง Pull Request พร้อมคำอธิบายและการตรวจตนเอง
- [ ] Lesson 1.4 ใช้ Semantic Versioning และ Tag
- [ ] ตรวจว่าไม่มี Secret, Token, Password หรือ Private Key ใน Repository

### เกณฑ์ผ่าน

- [x] มี Repository ที่อ่านเข้าใจ
- [ ] มี Feature Branch อย่างน้อยหนึ่ง Branch
- [ ] มี Pull Request อย่างน้อยหนึ่งรายการ
- [ ] แก้ Conflict ได้และอธิบายวิธีแก้ได้
- [ ] อธิบาย Commit History ได้
- [ ] ไม่มี Secret ใน Repository

**Git checkpoint:** `chore: establish repository workflow and contribution rules`  
**หลักฐาน/ลิงก์:** `https://github.com/jed220143/CICD_course.git`, commit `42b43f6`  
**วันที่ผ่าน:** 2026-07-15  

---

## Phase 2 — Backend แบบไม่ใช้ Docker ก่อน

### บทเรียนและงานลงมือทำ

- [ ] Lesson 2.1 สร้าง FastAPI Bootstrap และ Health Endpoint
- [ ] Lesson 2.2 อ่าน Configuration จาก Environment
- [ ] Lesson 2.3 เพิ่ม Structured Logging
- [ ] Lesson 2.4 เขียนและรัน Unit Test แรก
- [ ] อธิบายเส้นทาง Request ตั้งแต่ Client ถึง Process ได้

### เกณฑ์ผ่าน

- [ ] API รันบนเครื่องได้
- [ ] Health Endpoint ผ่าน
- [ ] Test ผ่าน
- [ ] Configuration อ่านจาก Environment
- [ ] อธิบายว่า Process ฟัง Port ได้อย่างไร

**Git checkpoint:** `feat(api): add application bootstrap and health endpoints`  
**หลักฐาน/ผลทดสอบ:**  
**วันที่ผ่าน:**  

---

## Phase 3 — Docker Fundamentals แบบหนึ่ง Container

### บทเรียนและงานลงมือทำ

- [ ] Lesson 3.1 เขียนและอธิบาย Dockerfile ทีละบรรทัด
- [ ] Lesson 3.2 เข้าใจ Build Context และสร้าง `.dockerignore`
- [ ] Lesson 3.3 ทดลอง Container Lifecycle, log และ exit code
- [ ] Lesson 3.4 ทดลองปัญหา Bind Address
- [ ] Lesson 3.5 ใช้ Non-root User และตรวจ Image Size
- [ ] อธิบาย Image, Container, Layer และ Cache ด้วยคำของตนเองได้

### เกณฑ์ผ่าน

- [ ] Build Image สำเร็จ
- [ ] Container รันได้
- [ ] เข้าถึง API ผ่าน Published Port ได้
- [ ] อธิบายความต่างของ `EXPOSE` กับ `-p` ได้
- [ ] อธิบาย Layer Cache ได้
- [ ] Container ไม่รันเป็น Root หากเหมาะสม

**Git checkpoint:** `build(api): containerize backend service`  
**หลักฐาน/ผลทดสอบ:**  
**วันที่ผ่าน:**  

---

## Phase 4 — PostgreSQL, Persistence และ Migration

### บทเรียนและงานลงมือทำ

- [ ] Lesson 4.1 ออกแบบ Data Model สำหรับ Telemetry
- [ ] Lesson 4.2 รัน PostgreSQL Container
- [ ] Lesson 4.3 ตั้งค่า Connection String โดยไม่ฝัง Secret ในโค้ด
- [ ] Lesson 4.4 สร้างและทดสอบ Alembic Migration
- [ ] Lesson 4.5 ทดลองลบ/สร้าง Container ใหม่และตรวจ Persistence
- [ ] Lesson 4.6 ทำ Readiness ที่ตรวจ Database จริง
- [ ] อธิบายผลกระทบก่อนลบ Volume หรือ Database ได้

### เกณฑ์ผ่าน

- [ ] API เชื่อม PostgreSQL ผ่าน Compose Network
- [ ] Migration ใช้งานได้
- [ ] Volume รักษาข้อมูลได้
- [ ] Readiness สะท้อนสถานะ Database จริง
- [ ] อธิบาย Data Loss Scenario ได้

**Git checkpoint:** `feat(storage): add PostgreSQL persistence and database migrations`  
**หลักฐาน/ผลทดสอบ:**  
**วันที่ผ่าน:**  

---

## Phase 5 — Multi-Container Compose และ Service Dependency

### บทเรียนและงานลงมือทำ

- [ ] Lesson 5.1 เขียน Compose Specification สำหรับ Core Stack
- [ ] Lesson 5.2 เพิ่ม Health Check
- [ ] Lesson 5.3 ทดลองและอธิบายว่า Startup ไม่เท่ากับ Ready
- [ ] Lesson 5.4 แยก Compose Profiles/Overrides ตาม Environment
- [ ] Lesson 5.5 ตรวจ Resource Usage และกำหนดขอบเขตที่เหมาะสม
- [ ] วาด Network Diagram พร้อม Port, Protocol และ Dependency

### เกณฑ์ผ่าน

- [ ] `docker compose up -d` ทำให้ Core Stack ทำงาน
- [ ] Health Status ถูกต้อง
- [ ] API Recover ได้เมื่อ Database กลับมา
- [ ] วาดและอธิบาย Network Diagram ได้
- [ ] อธิบาย Startup Order และ Readiness ได้

**Git checkpoint:** `build(compose): orchestrate API and database services`  
**หลักฐาน/ผลทดสอบ:**  
**วันที่ผ่าน:**  

---

## Phase 6 — MQTT Broker และ Device Simulator

### บทเรียนและงานลงมือทำ

- [ ] Lesson 6.1 อธิบาย MQTT, Topic, QoS และ Retain
- [ ] Lesson 6.2 รัน Mosquitto Container และตรวจการเชื่อมต่อ
- [ ] Lesson 6.3 สร้าง Device Simulator ส่ง Telemetry
- [ ] Lesson 6.4 ให้ Backend Subscribe และบันทึกข้อมูล
- [ ] Lesson 6.5 จัดการ Idempotency และ Duplicate Message
- [ ] Lesson 6.6 เปรียบเทียบ REST กับ MQTT และเลือกใช้ตามบริบท
- [ ] ทดลอง Payload ผิด Schema และ Broker/Network หลุด

### เกณฑ์ผ่าน

- [ ] Simulator ส่งข้อมูล
- [ ] Broker รับข้อมูล
- [ ] Backend บันทึกลง Database
- [ ] Payload ผิด Schema ถูกปฏิเสธและมี Log
- [ ] Reconnect ทำงาน
- [ ] อธิบาย QoS และ Duplicate ได้

**Git checkpoint:** `feat(telemetry): ingest simulated device data through MQTT`  
**หลักฐาน/ผลทดสอบ:**  
**วันที่ผ่าน:**  

---

## Phase 7 — REST API, Frontend และ Reverse Proxy

### บทเรียนและงานลงมือทำ

- [ ] Lesson 7.1 สร้าง Query API สำหรับ Telemetry
- [ ] Lesson 7.2 สร้าง Minimal Frontend แสดงข้อมูล
- [ ] Lesson 7.3 ตั้งค่า NGINX Reverse Proxy
- [ ] Lesson 7.4 ทดลอง CORS ก่อนและหลังใช้ Proxy
- [ ] Lesson 7.5 เพิ่ม Basic Security Headers
- [ ] Lesson 7.6 สร้าง Local Self-Signed HTTPS และให้ NGINX ทำ TLS Termination
- [ ] ตรวจว่า URL และ `localhost` ทุกจุดถูกต้องตามบริบทของ Client

### เกณฑ์ผ่าน

- [ ] Browser เข้า Entry Point เดียว
- [ ] Frontend เรียก API ผ่าน Proxy
- [ ] ไม่มีการ Hardcode `localhost` ที่ผิดบริบท
- [ ] API Error แสดงผลเหมาะสม
- [ ] อธิบาย Reverse Proxy และ CORS ได้
- [ ] เข้า Local NGINX ผ่าน Self-Signed HTTPS ได้
- [ ] อธิบาย Encryption กับ Public Trust ได้ และไม่มี Private Key ใน Git

**Git checkpoint:** `feat(web): add dashboard and NGINX reverse proxy`  
**หลักฐาน/ภาพหน้าจอ:**  
**วันที่ผ่าน:**  

---

## Phase 8 — Testing, Code Quality และ Security Scan

### บทเรียนและงานลงมือทำ

- [ ] Lesson 8.1 ออกแบบ Testing Pyramid
- [ ] Lesson 8.2 เพิ่ม Database Integration Test
- [ ] Lesson 8.3 เพิ่ม MQTT Integration Test
- [ ] Lesson 8.4 ตั้งค่า Lint และ Format
- [ ] Lesson 8.5 ตั้งค่า Type Checking
- [ ] Lesson 8.6 ทำ Dependency Scan และ Container Scan
- [ ] สร้างคำสั่งเดียวสำหรับตรวจคุณภาพ เช่น `make check`
- [ ] อ่านผล Scan และแยก Critical issue ออกจาก Warning ได้

### เกณฑ์ผ่าน

- [ ] Unit Test ผ่าน
- [ ] Integration Test ผ่าน
- [ ] Lint ผ่าน
- [ ] Scan ทำงานและอ่านผลได้
- [ ] มีคำสั่งเดียวสำหรับตรวจคุณภาพ

**Git checkpoint:** `test: add automated quality and integration checks`  
**หลักฐาน/ผลทดสอบ:**  
**วันที่ผ่าน:**  

---

## Phase 9 — Continuous Integration ด้วย GitHub Actions

### บทเรียนและงานลงมือทำ

- [ ] Lesson 9.1 สร้าง CI Workflow แรก
- [ ] Lesson 9.2 รัน Integration Test ด้วย Service Container หรือ Compose
- [ ] Lesson 9.3 ใช้ Cache อย่างถูกต้อง
- [ ] Lesson 9.4 Build Docker Image ใน CI
- [ ] Lesson 9.5 รัน Security Scan ใน CI
- [ ] Lesson 9.6 ตั้ง Branch Protection
- [ ] ทำให้ Test หรือตัว Lint ล้มโดยตั้งใจและอ่าน Failure Log

### เกณฑ์ผ่าน

- [ ] Pull Request แสดง CI Status
- [ ] CI Fail เมื่อ Test Fail
- [ ] CI Fail เมื่อ Lint Fail
- [ ] Docker Build ผ่าน
- [ ] Scan ทำงาน
- [ ] อธิบาย Runner, Job, Step และ Artifact ได้

**Git checkpoint:** `ci: validate code and container builds on every pull request`  
**หลักฐาน/Workflow run:**  
**วันที่ผ่าน:**  

---

## Phase 10 — Container Registry และ Release Management

### บทเรียนและงานลงมือทำ

- [ ] Lesson 10.1 กำหนด Image Naming Convention
- [ ] Lesson 10.2 กำหนด Tag Strategy ที่ไม่พึ่ง `latest` อย่างเดียว
- [ ] Lesson 10.3 ตั้ง Registry Authentication ผ่าน Secret
- [ ] Lesson 10.4 สร้าง Release Workflow
- [ ] Lesson 10.5 พิสูจน์ Reproducibility และ Traceability
- [ ] ทดสอบ Pull และ Run Image จาก Environment ใหม่

### เกณฑ์ผ่าน

- [ ] Registry มี Versioned Image
- [ ] Image เชื่อมโยงกลับไปยัง Commit ได้
- [ ] ไม่มี Password ใน Workflow
- [ ] Pull และ Run Image บนเครื่องใหม่ได้
- [ ] อธิบาย Artifact และ Immutability ได้

**Git checkpoint:** `ci(release): publish versioned container images`  
**หลักฐาน/Image tag:**  
**วันที่ผ่าน:**  

---

## Phase 11 — Cloud Foundation แบบ Free-tier Gated

> จุดหยุดด้านความปลอดภัย: ห้ามสร้าง AWS Resource จนกว่า `docs/aws-free-tier-gate.md` จะ PASS หากไม่ผ่านให้ใช้ Local Simulation

### บทเรียนและงานลงมือทำ

- [ ] ตรวจ Free account plan, Credit และวันหมดอายุใน AWS Billing Console
- [ ] ทำ `docs/aws-free-tier-gate.md` และเลือก PASS หรือ LOCAL-ONLY
- [ ] Lesson 11.1 อธิบาย Cloud Mental Model
- [ ] Lesson 11.2 เรียน IAM/Least Privilege และเปิด Root MFA หากใช้ AWS
- [ ] Lesson 11.3 ใช้ Local Target ก่อน แล้วทำ EC2 เมื่อ Gate ผ่าน
- [ ] Lesson 11.4 ทดลอง Local Port Exposure/Security Group
- [ ] Lesson 11.5 ทำ Zero-cost และ Destroy Drill
- [ ] วาด Mapping ระหว่าง Local Lab กับ VPC/Subnet/Security Group/EC2

### เกณฑ์ผ่าน

- [ ] Local Simulation ผ่าน หรือ AWS Gate ผ่านพร้อมหลักฐานครบ
- [ ] มี Cloud Architecture Diagram และ IAM Policy ตัวอย่าง
- [ ] เข้า Local Linux Deployment Target ได้ และเข้า EC2 ได้เมื่อ Gate ผ่าน
- [ ] Published Port เปิดเท่าที่จำเป็น
- [ ] อธิบาย VPC, Subnet และ Security Group ระดับพื้นฐานได้
- [ ] ทำ Local Cleanup Checklist ได้
- [ ] อธิบายข้อจำกัดของ Local Simulation เมื่อเทียบกับ AWS ได้
- [ ] หากทำ AWS Lab: ค่าใช้จ่ายจริง 0 บาทและไม่มี Resource ค้าง

**Git checkpoint:** `docs(cloud): document free-tier gate and zero-cost cloud lab`  
**ค่าใช้จ่าย Cloud (ต้องเป็น 0 บาท)/หลักฐาน:**  
**วันที่ผ่าน:**  

---

## Phase 12 — Continuous Delivery แบบ Local-first และ AWS Credit-gated

### บทเรียนและงานลงมือทำ

- [ ] Lesson 12.1 Deploy Production แบบ Manual และบันทึกขั้นตอน
- [ ] Lesson 12.2 สร้าง Production Compose
- [ ] Lesson 12.3 สร้าง Deployment Script ที่ตรวจสอบผลได้
- [ ] Lesson 12.4 ทำ Local CD และ Optional AWS CD เมื่อ Gate ผ่าน
- [ ] Lesson 12.5 จัดการ Secret โดยไม่เก็บใน Git/Log
- [ ] Lesson 12.6 ทดลอง Rollback ไป Version ก่อนหน้า
- [ ] เพิ่ม Health Validation หลัง Deploy

### เกณฑ์ผ่าน

- [ ] Deploy Version ใหม่ได้
- [ ] Pipeline ไม่ใช้ `latest` อย่างเดียว
- [ ] Secret ไม่รั่ว
- [ ] Health Check หลัง Deploy ทำงาน
- [ ] Rollback ได้
- [ ] อธิบาย Continuous Delivery กับ Continuous Deployment ได้

**Git checkpoint:** `cd: deploy locally and validate optional free-tier target`  
**หลักฐาน/Deployment run:**  
**วันที่ผ่าน:**  

---

## Phase 13 — Observability, Backup และ Incident Practice

### บทเรียนและงานลงมือทำ

- [ ] Lesson 13.1 อธิบาย Log, Metric และ Trace
- [ ] Lesson 13.2 เพิ่ม Application Metrics
- [ ] Lesson 13.3 สร้าง Local Monitoring Stack และ Dashboard
- [ ] Lesson 13.4 จัดการและค้นหา Log
- [ ] Lesson 13.5 ทำ Database Backup
- [ ] Lesson 13.6 Restore ลง Environment ทดสอบและตรวจข้อมูล
- [ ] Lesson 13.7 จำลอง Incident ด้วยกรอบ O-H-T-F
- [ ] เขียน Incident Report พร้อม Root Cause และ Prevention

### เกณฑ์ผ่าน

- [ ] มี Dashboard/Metric ขั้นพื้นฐานใน Local
- [ ] Log อ่านและค้นหาได้
- [ ] Backup สำเร็จ
- [ ] Restore สำเร็จและตรวจความถูกต้องของข้อมูลแล้ว
- [ ] มี Incident Report อย่างน้อยหนึ่งฉบับ
- [ ] อธิบาย Root Cause และ Prevention ได้

**Git checkpoint:** `ops: add monitoring, backup, restore and incident runbooks`  
**หลักฐาน/Runbook:**  
**วันที่ผ่าน:**  

---

## Phase 14 — Kubernetes แบบ Local-first และ Infrastructure as Code

### Part A — Kubernetes Local

- [ ] Lesson 14.1 Mapping แนวคิด Compose กับ Kubernetes
- [ ] Lesson 14.2 Deploy Pod และ Deployment
- [ ] Lesson 14.3 ใช้ Service Discovery
- [ ] Lesson 14.4 ใช้ ConfigMap และ Secret
- [ ] Lesson 14.5 ตั้ง Readiness/Liveness Probe
- [ ] Lesson 14.6 Scale Replica และสังเกตผล
- [ ] Lesson 14.7 ทดลอง Rolling Update และ Rollback
- [ ] Lesson 14.8 อธิบายแนวทาง Persistent Data

### Part B — Terraform

- [ ] Lesson 14.9 อธิบาย Infrastructure as Code, State และ Drift
- [ ] Lesson 14.10 เขียน Local Resource และ Optional AWS Definition
- [ ] Lesson 14.11 ทำ Terraform Destroy Drill
- [ ] ยืนยันว่าไม่สร้าง EKS ใน Free-first Track

### เกณฑ์ผ่าน

- [ ] Deploy API บน Local Kubernetes ได้
- [ ] Scale Replica ได้
- [ ] Probe ทำงาน
- [ ] Rolling Update และ Rollback ได้
- [ ] อธิบายว่า Pod ต่างจาก Container ได้
- [ ] Terraform Plan/Apply/Destroy กับ Local Resource ได้
- [ ] อธิบาย State และ Drift ได้
- [ ] ไม่มี EKS ที่สร้างโดยไม่จำเป็น
- [ ] หากทำ AWS Terraform Lab: Gate ยังผ่าน ค่าใช้จ่ายจริง 0 บาท และ Destroy ครบ

**Git checkpoint:** `feat(platform): add local Kubernetes and infrastructure-as-code labs`  
**หลักฐาน/ผลทดสอบ:**  
**วันที่ผ่าน:**  

---

## Final — Capstone Exam

### ความพร้อมก่อนสอบ

- [ ] Milestone M1–M12 ผ่านครบ
- [ ] ระบบสร้างใหม่จากเอกสารได้
- [ ] Test, Lint และ Scan ผ่าน
- [ ] Deploy และ Rollback ได้
- [ ] Backup และ Restore ผ่านการทดสอบ
- [ ] Monitoring ตอบได้ว่าเกิดอะไร ที่ไหน และตั้งแต่เมื่อไร
- [ ] ไม่มี Secret ใน Repository หรือ Log
- [ ] ยืนยันว่าไม่มี Cloud Resource และค่าใช้จ่าย Cloud เป็น 0 บาท

### ความเข้าใจที่ต้องอธิบายได้

- [ ] Architecture และ Data Flow ทั้งระบบ
- [ ] Network, Port, Protocol และ Dependency ของแต่ละ Service
- [ ] Git Workflow, CI, CD และ Release Strategy
- [ ] Image, Container, Compose และ Kubernetes
- [ ] Persistence, Migration, Backup และ Restore
- [ ] Health Check, Readiness, Monitoring และ Incident Response
- [ ] Security, Secret Management และ Cloud Cost Safety
- [ ] Trade-off และข้อจำกัดของ Architecture ปัจจุบัน

### ผลสอบ

| รายการ | ผล/คะแนน | หมายเหตุ |
|---|---:|---|
| ระบบทำงานตาม Scenario |  |  |
| การ Debug ด้วย O-H-T-F |  |  |
| การอธิบาย Architecture |  |  |
| Security และ Cost Safety |  |  |
| เอกสารและ Portfolio |  |  |

**ผลสุดท้าย:** [ ] ผ่าน  [ ] ต้องทบทวน  
**วันที่สอบ:**  
**หัวข้อที่ต้องปรับปรุง:**  

---

## Checklist เอกสารและ Portfolio เมื่อจบ

- [ ] `README.md` — Project Overview
- [ ] Architecture Diagram
- [ ] Data Flow
- [ ] Local Setup
- [ ] Test Instructions
- [ ] CI/CD Overview
- [ ] Deployment Guide
- [ ] Screenshots
- [ ] Security Considerations
- [ ] Cost Safety
- [ ] Known Limitations
- [ ] Future Improvements
- [ ] `docs/learning-log.md`
- [ ] ADR สำหรับการตัดสินใจด้าน Architecture ที่สำคัญ
- [ ] Runbook สำหรับ Deploy, Rollback, Backup, Restore และ Incident
- [ ] ตรวจลิงก์ คำสั่ง และขั้นตอนทั้งหมดจากเครื่อง/Environment ใหม่

## แบบบันทึกประจำ Session

คัดลอกส่วนนี้ไปต่อท้าย `docs/learning-log.md` ทุกครั้งที่เรียน

```markdown
## Session: YYYY-MM-DD — Phase X / Lesson X.X

- เป้าหมายวันนี้:
- สิ่งที่ทำสำเร็จ:
- คำสั่งสำคัญและสิ่งที่คำสั่งนั้นตรวจ:
- สิ่งที่เข้าใจและอธิบายด้วยคำของตนเอง:
- ปัญหา/อาการที่พบ:
- Observe:
- Hypotheses:
- Test:
- Fix and Verify:
- Root Cause:
- สิ่งที่ป้องกันการเกิดซ้ำ:
- หลักฐาน (commit/PR/log/screenshot):
- คำถามที่ยังค้าง:
- งานถัดไป:
```

## ทบทวนราย Phase

ก่อนอนุมัติให้ผ่านแต่ละ Phase ให้ตอบคำถามต่อไปนี้

- [ ] ฉันสร้างหรือทำซ้ำส่วนนี้ได้โดยไม่ Copy/Paste แบบไม่เข้าใจ
- [ ] ฉันอธิบายเหตุผลของไฟล์และ Configuration สำคัญได้
- [ ] ฉันอ่านผลลัพธ์และแยก Success, Warning และ Failure ได้
- [ ] ฉันตั้งสมมติฐานก่อนแก้ปัญหา และเปลี่ยนตัวแปรทีละอย่าง
- [ ] ฉันทดสอบ Regression หลังแก้ไขแล้ว
- [ ] ฉันบันทึกสิ่งที่เรียนรู้และหลักฐานแล้ว
- [ ] ฉัน Commit งานด้วยข้อความที่สื่อความหมายแล้ว
- [ ] Acceptance Criteria ของ Phase ผ่านครบทุกข้อ
