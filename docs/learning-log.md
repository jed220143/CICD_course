# Learning Log — Mini Telemetry Platform

ไฟล์นี้ใช้บันทึกความเข้าใจ การทดลอง ปัญหา และหลักฐานการเรียนรู้ตลอดหลักสูตร

## Session: 2026-07-13 — Phase 0 / Lesson 0.1–0.3

### เป้าหมายวันนี้

- ตรวจ Environment ที่จะใช้เรียน
- เก็บ Baseline ความรู้ก่อนเริ่มสร้างระบบ
- ยืนยันกฎ Cost Safety ก่อนใช้ Cloud

### Environment Audit

| รายการ | ผลตรวจ | สถานะ/หมายเหตุ |
|---|---|---|
| OS | Windows 11 Education, Build 26200, x64 | พร้อมใช้งาน |
| RAM | 15,523 MB; ว่างขณะตรวจ 2,689 MB | ควรปิดโปรแกรมที่ไม่จำเป็นก่อนรันหลาย Container |
| Disk C | ทั้งหมด 414.85 GB; ว่าง 136.04 GB | พร้อมใช้งาน |
| Git | 2.41.0.windows.1 | พร้อมใช้งาน |
| Docker CLI | 29.5.3 | พร้อมใช้งาน |
| Docker Engine | 29.5.3, Linux/x86_64, 12 CPU, RAM ประมาณ 7.34 GB | พร้อมใช้งาน |
| Docker Compose | v5.1.4 | พร้อมใช้งาน |
| Python | 3.11.5 | พร้อมใช้งาน |
| OpenSSH | 9.5p2 | พร้อมใช้งาน |
| TCP port 3306 | มี Process ฟังอยู่ | อาจชนกับ MySQL Container ในอนาคต |
| TCP port 5432 | มี Process ฟังอยู่ | อาจชนกับ PostgreSQL Container ในอนาคต |

### สิ่งที่สังเกตได้

- เครื่องมือหลักติดตั้งครบและ Docker daemon ตอบสนอง
- RAM ที่ว่างขณะตรวจค่อนข้างน้อยเมื่อเทียบกับงานหลาย Container
- Port มาตรฐานของ MySQL และ PostgreSQL ถูกใช้งานอยู่แล้ว
- เมื่อเริ่ม Lab Database ต้องตรวจ Process เดิมก่อน และเลือกว่าจะหยุด Service เดิมหรือเปลี่ยน Published Port โดยไม่ลบข้อมูล

## Baseline Quiz — ให้ผู้เรียนตอบด้วยคำของตนเอง

คำตอบไม่จำเป็นต้องถูกทั้งหมด จุดประสงค์คือบันทึกความเข้าใจก่อนเรียน ห้ามค้นหรือให้ AI เขียนคำตอบแทนในรอบแรก

### 1. Image ต่างจาก Container อย่างไร

**Baseline ของผู้เรียน:** ยังไม่ได้อธิบาย ขอรับคำอธิบายสั้น ๆ

**คำอธิบายหลังทำ Baseline:** Image คือแม่แบบแบบอ่านอย่างเดียวที่บรรจุโปรแกรมและสิ่งที่ต้องใช้ ส่วน Container คือ Instance ที่กำลังรันจาก Image และมีสถานะของตนเอง

### 2. Port ภายใน Container กับ Port ที่ Publish ออกมาที่ Host ต่างกันอย่างไร

**Baseline ของผู้เรียน:** ยังไม่ได้อธิบาย ขอรับคำอธิบายสั้น ๆ

**คำอธิบายหลังทำ Baseline:** Port ภายในคือจุดที่โปรแกรมฟังอยู่ใน Network ของ Container ส่วน Published Port คือ Port บน Host ที่ส่ง Traffic เข้าไปยัง Port ภายใน เช่น `8080:8000`

### 3. Volume มีไว้ทำอะไร

**Baseline ของผู้เรียน:** ยังไม่รู้

**คำอธิบายหลังทำ Baseline:** Volume ใช้เก็บข้อมูลแยกจากอายุของ Container ทำให้ลบและสร้าง Container ใหม่แล้วข้อมูลสำคัญ เช่นข้อมูล Database ยังอยู่

### 4. `localhost` ภายใน Container หมายถึงอะไร

**Baseline ของผู้เรียน:** ยังไม่ได้อธิบาย ขอรับคำอธิบายสั้น ๆ

**คำอธิบายหลังทำ Baseline:** `localhost` หมายถึง Container ตัวนั้นเอง ไม่ใช่เครื่อง Host และไม่ใช่ Container ตัวอื่น

### 5. Git Commit, Push และ Pull Request ต่างกันอย่างไร

**Baseline ของผู้เรียน:** ยังไม่ได้อธิบาย ขอรับคำอธิบายสั้น ๆ

**คำอธิบายหลังทำ Baseline:** Commit บันทึกชุดการเปลี่ยนแปลงใน Repository บนเครื่อง, Push ส่ง Commit ไป Remote และ Pull Request ขอให้นำการเปลี่ยนแปลงจาก Branch หนึ่งไปรวมอีก Branch พร้อมพื้นที่สำหรับ Review และ CI

### 6. CI และ CD ต่างกันอย่างไร

**Baseline ของผู้เรียน:** ยังไม่รู้

**คำอธิบายหลังทำ Baseline:** CI ตรวจการเปลี่ยนแปลงอัตโนมัติ เช่น Test, Lint และ Build ส่วน CD นำ Artifact ที่ผ่าน CI ไปส่งมอบหรือ Deploy ต่ออย่างเป็นระบบ

## สรุปหลังตอบ Baseline

- หัวข้อที่มั่นใจ: ยังไม่ได้ระบุ
- หัวข้อที่ยังไม่มั่นใจ: Volume และความแตกต่างระหว่าง CI/CD
- คำถามที่อยากได้คำตอบจากหลักสูตร:
- ยืนยันว่าอ่านและยอมรับ `docs/cost-safety.md` ฉบับ No-spend แล้ว: [x]
- ยืนยันว่าขณะนี้ยังไม่ได้สร้าง AWS Resource สำหรับหลักสูตรนี้: [x]

### การตัดสินใจด้านแผนการเรียน

- ผู้เรียนกำหนดงบ Cloud ปัจจุบันเป็น 0 บาท
- ยังไม่มี HTTPS/Domain และไม่ต้องการมีค่าใช้จ่ายในตอนนี้
- ปรับ Phase 11–12 เป็น Local Simulation และ Local CD
- HTTP ใช้เฉพาะ Local Lab และจะไม่เปิดสู่ Public Internet
- การตัดสินใจเดิม (ถูกแทนที่แล้ว): เลื่อน AWS, Public Deployment, Domain และ HTTPS เป็น Deferred Lab

### Revision: Free-guaranteed Core + Credit-gated AWS

- ปรับให้ Self-Signed HTTPS บน Local เป็นบทบังคับโดยไม่เสียเงิน
- ทุก Learning Outcome และ Capstone ผ่านได้ด้วย Local Track
- เพิ่ม AWS Hands-on เฉพาะเมื่อ Free account plan และ `docs/aws-free-tier-gate.md` ผ่าน
- ห้าม Upgrade เป็น Paid plan และห้ามใช้ Service เสี่ยงค่าใช้จ่าย
- นโยบายฉบับนี้รอผู้เรียนตรวจและยอมรับ

### AWS Free Tier Preliminary Check

- วันที่สมัคร: 2026-07-13
- Plan ที่เลือก: Free account plan
- Credit เริ่มต้น: USD 100.00
- Credit ที่ใช้แล้ว: USD 0.00
- Credit หมดอายุ: 2027-07-13
- ไม่บันทึก Account ID, Credit ID หรือข้อมูลการชำระเงิน
- ยังไม่สร้าง AWS Resource
- Free Tier Gate ยังไม่ PASS; ต้องตรวจ MFA, Account plan, Free plan expiration, Budget และ Billing ซ้ำก่อน Phase 11
- ผู้เรียนยอมรับนโยบาย Free-guaranteed/Credit-gated และให้เริ่ม Phase 1

## Session: 2026-07-13 — Phase 1 / Lesson 1.1

### สิ่งที่ทำแล้ว

- สร้าง `README.md` เป็นหน้าแนะนำ Repository
- สร้าง `.gitignore` เพื่อกัน Environment file, Secret, Private Key, Log, Cache และ Terraform State
- สร้าง `.env.example` สำหรับบอกชื่อ Configuration โดยไม่มี Secret
- เริ่ม Git Repository บน Branch `main`
- ยังไม่ได้ Stage หรือ Commit เพื่อให้ผู้เรียนตรวจ Working Tree ก่อน

### ผล `git status --short`

```text
?? .env.example
?? .gitignore
?? "Lesson plan/"
?? README.md
?? docs/
```

`??` หมายถึงไฟล์ยังเป็น Untracked และยังไม่อยู่ใน Staging Area หรือ Commit History

### Security Check

- `.env` ถูก Ignore
- `.env.example` ไม่ถูก Ignore และควร Commit
- `*.pem`, `*.key` และ `*.log` ถูก Ignore
- `.terraform.lock.hcl` ควร Commit เพื่อให้ Provider version ทำซ้ำได้ จึงไม่ถูก Ignore
- ตรวจ Repository แล้วไม่พบ AWS Account ID, Access Key pattern, Secret field หรือ Private Key header
- ใช้ GitHub `noreply` email ใน Local Repository เพื่อไม่เปิดเผยอีเมลจริงใน Commit

## หลักฐาน

- Environment Audit: บันทึกใน Session นี้
- Initial Commit: `42b43f6` — `chore: initialize learning documentation and cost safety policy`
- Remote Repository: `https://github.com/jed220143/CICD_course.git`
- Push Status: `main` push สำเร็จและ track `origin/main` แล้ว
- Pull Request: ยังไม่มี จะทำใน Lesson 1.3 หลังฝึก Branch Workflow

## Session: 2026-07-15 — Phase 1 / Lesson 1.2

### สิ่งที่ทำแล้ว

- ยืนยันว่า GitHub account กลับมาใช้งานได้และ push ไป `origin/main` สำเร็จ
- สร้าง branch `feature/repository-workflow` เพื่อฝึก Short-lived Feature Branch
- เพิ่ม `CONTRIBUTING.md` สำหรับกติกา Branch, Commit, Pull Request และ Safety Rules
- เพิ่ม `.github/PULL_REQUEST_TEMPLATE.md` สำหรับฝึกเปิด Pull Request แบบมี Scope, Test Evidence, Risk และ Rollback

### หลักฐาน

- Remote Repository: `https://github.com/jed220143/CICD_course.git`
- Base branch: `main`
- Feature branch: `feature/repository-workflow`

## Session: 2026-07-15 — Phase 1 / Lesson 1.3

### สิ่งที่ทำแล้ว

- เปิด Pull Request จาก `feature/repository-workflow` เข้า `main`
- ใช้ Pull Request template เพื่อฝึกเขียน Summary, Scope, Test Evidence, Risk และ Rollback
- ยังไม่ Merge ทันที เพื่อใช้ PR เป็นจุดเรียน Review และตรวจหลักฐานก่อนรวมเข้า `main`

### หลักฐาน

- Pull Request branch: `feature/repository-workflow`
- Base branch: `main`
- Pull Request URL: `https://github.com/jed220143/CICD_course/pulls`
- Merge commit: `214d038` — `Merge pull request #1 from jed220143/feature/repository-workflow`
- Local `main` fast-forward แล้วหลัง merge

### Commit History ที่อธิบายได้

- `42b43f6`: commit เริ่มต้นของเอกสารและ safety policy
- `171ea90`: บันทึกหลักฐานว่าเชื่อม GitHub remote และ push `main` สำเร็จ
- `547ea12`, `a8cc249`, `777231e`: งานบน feature branch สำหรับ workflow และ PR evidence
- `214d038`: merge commit ที่รวม PR #1 เข้า `main`

## Session: 2026-07-15 — Phase 1 / Lesson 1.2 Conflict Lab

### สิ่งที่ทำแล้ว

- สร้าง branch `feature/conflict-main-rule` และแก้บรรทัด Commit Guidelines ใน `CONTRIBUTING.md`
- สร้าง branch `feature/conflict-safety-rule` และแก้บรรทัดเดียวกันอีกแบบ
- merge `feature/conflict-main-rule` เข้า `feature/conflict-safety-rule` เพื่อให้เกิด conflict จริง
- แก้ conflict โดยรวมความหมายทั้งสองฝั่งเข้าด้วยกัน

### วิธีแก้ Conflict ที่ใช้

1. อ่าน marker `<<<<<<<`, `=======`, `>>>>>>>` เพื่อแยกฝั่งปัจจุบันกับฝั่งที่ merge เข้ามา
2. เลือกผลลัพธ์สุดท้ายที่เก็บ intent สำคัญของทั้งสองฝั่ง
3. ลบ conflict marker ทั้งหมด
4. ใช้ `git add CONTRIBUTING.md` เพื่อ mark resolved
5. commit ผลการแก้ด้วย `docs: resolve commit guidance conflict`

### หลักฐาน

- Conflict branch: `feature/conflict-safety-rule`
- Other branch: `feature/conflict-main-rule`
- Conflict resolution commit: `6253553`
- Merge commit: `5976e0d` — `Merge pull request #2 from jed220143/feature/conflict-safety-rule`
- Local `main` fast-forward แล้วหลัง merge

### Secret Scan หลัง PR #2

- ตรวจ pattern ของ AWS Access Key, AWS Secret Access Key, Private Key header, password, token และ secret แล้ว
- ผลลัพธ์: ไม่พบ secret pattern ใน repository
