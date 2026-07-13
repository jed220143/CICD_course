# Cloud Cost and Resource Safety Policy

เอกสารนี้เป็นกฎบังคับสำหรับการใช้ Cloud ในโปรเจกต์ Mini Telemetry Platform

## หลักการ

1. เรียนแบบ Local-first และใช้ Cloud เฉพาะ Phase ที่กำหนด
2. เป้าหมายค่าใช้จ่ายจริงคือ **0 บาท** ทุก Learning Outcome ต้องทำ Local ได้
3. AWS Hands-on ทำได้เฉพาะเมื่อ `docs/aws-free-tier-gate.md` ผ่านและผู้เรียนยืนยันก่อนสร้าง Resource
4. ก่อนสร้าง Resource ต้องทราบราคาโดยประมาณ, Owner, Purpose และวิธีทำลาย
5. ใช้ Free Tier/Free-first เมื่อเหมาะสม แต่ไม่ถือว่าคำว่า Free Tier แปลว่าจะไม่มีค่าใช้จ่าย
6. หลีกเลี่ยง Managed Service ราคาแพงในเส้นทางหลัก
7. Kubernetes บน AWS เป็น Optional; เส้นทางหลักใช้ Local Kubernetes
8. ไม่ซื้อ Domain; Public Deployment เป็น Lab ชั่วคราวเฉพาะ Free account plan ที่ Gate ผ่าน
9. ใช้ HTTP ได้เฉพาะ `localhost` หรือเครือข่าย Lab ที่เชื่อถือได้ ห้ามส่ง Credential/Secret ผ่าน HTTP และห้ามเปิด HTTP สู่ Public Internet
10. Self-Signed HTTPS/TLS บน Local เป็นบทบังคับ; Publicly Trusted HTTPS เป็น Optional
11. ห้าม Upgrade เป็น Paid plan หรือเข้าร่วม AWS Organizations ระหว่างหลักสูตร
12. Budget Alert ไม่ใช่ Hard Limit จึงห้ามใช้แทน Free-tier Gate และ Destroy Plan

## Resource ที่ห้ามสร้างโดยยังไม่ศึกษาค่าใช้จ่าย

- NAT Gateway
- Amazon EKS
- Amazon RDS
- Application/Network Load Balancer
- Resource อื่นที่คิดค่าบริการต่อชั่วโมง ต่อปริมาณข้อมูล หรือมี Resource ลูกที่คิดเงิน

## Checklist ก่อนสร้าง Cloud Resource

- [ ] `docs/aws-free-tier-gate.md` มีผลเป็น PASS
- [ ] Billing Console ยืนยันว่าเป็น Free account plan และไม่คิดเงินจนกว่าจะ Upgrade
- [ ] อยู่ใน Phase ที่อนุญาตให้ใช้ Cloud
- [ ] Root account เปิด MFA แล้ว
- [ ] ตั้ง Budget และ Cost Alert แล้ว
- [ ] ตรวจ Pricing และประมาณค่าใช้จ่ายแล้ว
- [ ] ระบุ Region แล้ว
- [ ] ระบุ Owner แล้ว
- [ ] ระบุ Purpose แล้ว
- [ ] กำหนดเวลาสิ้นสุด Lab แล้ว
- [ ] เขียน Destroy Plan แล้ว
- [ ] ตรวจว่าค่าใช้จ่ายของ Resource ลูก เช่น Storage, IP, Snapshot และ Data Transfer แล้ว
- [ ] ไม่มี Secret, Password, Token หรือ Private Key ที่จะถูก Commit ลง Git

## Tag ขั้นต่ำ

Cloud Resource ทุกตัวที่รองรับ Tag ต้องมีอย่างน้อย:

| Tag | ตัวอย่าง |
|---|---|
| `Project` | `mini-telemetry-platform` |
| `Owner` | ชื่อหรือรหัสผู้เรียน |
| `Environment` | `learning` |
| `Purpose` | `phase-11-ec2-lab` |
| `DestroyAfter` | วันที่ในรูปแบบ `YYYY-MM-DD` |

## Checklist หลังจบ Cloud Lab

- [ ] ปิดหรือลบ Compute Resource ที่ไม่ใช้แล้ว
- [ ] ลบ Storage, Volume, Snapshot หรือ IP ที่ไม่ต้องเก็บ
- [ ] ตรวจว่าไม่มี Resource ลูกตกค้าง
- [ ] ตรวจ Billing Dashboard และ Cost Explorer
- [ ] ตรวจ Resource ในทุก Region ที่เคยใช้
- [ ] บันทึกผลการทำลายและค่าใช้จ่ายจริงใน Learning Log
- [ ] หากต้องเก็บ Resource ไว้ ระบุเหตุผล ค่าใช้จ่าย และวันที่ตรวจครั้งถัดไป

## กฎป้องกันข้อมูลสูญหาย

- ห้ามลบ Volume, Database, Snapshot หรือ State File เพื่อแก้ปัญหาโดยไม่ทราบผลกระทบ
- ก่อนทำลาย Resource ที่มีข้อมูล ต้องระบุว่าข้อมูลใดจะหายและจำเป็นต้อง Backup หรือไม่
- Backup จะถือว่าใช้ได้เมื่อผ่าน Restore Test แล้วเท่านั้น
- Terraform State ต้องได้รับการปกป้องและห้ามแก้ด้วยมือโดยไม่เข้าใจผลกระทบ

## บันทึกการยอมรับ

ผู้เรียนยืนยันว่าอ่าน เข้าใจ และจะปฏิบัติตามนโยบายนี้ก่อนใช้ Cloud

- ชื่อผู้เรียน: ผู้เรียนโปรเจกต์ CICD_study
- วันที่: 2026-07-13
- ยอมรับนโยบาย Free-guaranteed/Credit-gated ฉบับปรับปรุง: [x]
