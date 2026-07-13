# AWS Free Tier Gate — ห้ามสร้าง Resource ก่อนผ่าน

เอกสารนี้เป็น Safety Gate สำหรับ AWS Hands-on ของ Mini Telemetry Platform เป้าหมายคือ **ค่าใช้จ่ายจริง 0 บาท**

> หากตรวจข้อใดไม่ได้หรือสถานะไม่ชัดเจน ให้เลือก `LOCAL-ONLY` ทันที ห้ามเดาและห้าม Upgrade เป็น Paid plan

## ข้อมูลตรวจสอบ

ห้ามบันทึก Account ID, Card, Access Key, Secret Key หรือข้อมูลลับในไฟล์นี้

| รายการ | ค่าที่ตรวจพบ |
|---|---|
| วันที่ตรวจ | 2026-07-13 (Preliminary check) |
| วันที่สร้างบัญชีโดยประมาณ | 2026-07-13 |
| Plan ที่เลือกตอนสมัคร | Free account plan |
| Credit คงเหลือ | USD 100.00; ใช้แล้ว USD 0.00 |
| วันหมดอายุ Credit | 2027-07-13 |
| วันหมดอายุ Free plan | ต้องตรวจซ้ำจาก Billing Console ก่อน Phase 11 |
| Region สำหรับ Lab |  |
| ระยะเวลา EC2 Lab ที่วางแผน |  |
| ค่าใช้จ่ายประมาณการก่อนใช้ Credit |  |

## Gate A — Account Safety

สถานะปัจจุบัน: **ยังไม่ PASS** — บันทึกเครดิตเบื้องต้นแล้ว แต่ต้องตรวจ Account plan, วันหมดอายุ, MFA, Budget และ Billing ซ้ำก่อน Phase 11

- [ ] Billing Console แสดงว่าเป็น **Free account plan**
- [ ] Console ระบุว่าจะไม่เกิดค่าใช้จ่ายจนกว่าจะ Upgrade
- [ ] ยังไม่หมดระยะ Free plan และ Credit
- [ ] Credit คงเหลือมากกว่าค่าใช้จ่ายประมาณการอย่างเพียงพอ
- [ ] บัญชีไม่ได้อยู่ใน AWS Organizations
- [ ] จะไม่ Upgrade เป็น Paid plan ระหว่างหลักสูตร
- [ ] Root เปิด MFA แล้ว
- [ ] เปิด Free Tier Usage Alert แล้ว
- [ ] สร้าง Zero-spend/Cost Budget Alert แล้ว

## Gate B — Resource Safety

- [ ] ตรวจราคา EC2, EBS, Public IPv4 และ Data Transfer จากหน้า AWS ปัจจุบันแล้ว
- [ ] ใช้เฉพาะ Service/Feature ที่ Free account plan อนุญาต
- [ ] ไม่ใช้ NAT Gateway, RDS, EKS, Load Balancer หรือ Marketplace
- [ ] ใช้ข้อมูลจำลอง ไม่มีข้อมูลจริงหรือ Secret ผ่าน Public HTTP
- [ ] SSH จำกัด Source IP ของผู้เรียน
- [ ] กำหนดเวลาจบ Lab และตั้ง Reminder แล้ว
- [ ] มีคำสั่ง/ขั้นตอน Health Check และ Rollback
- [ ] มี Destroy Checklist ครอบคลุม EC2, EBS, Snapshot และ Public/Elastic IP
- [ ] Backup Artifact/เอกสารที่ต้องเก็บออกจาก AWS แล้ว

## คำตัดสิน

- [ ] **PASS** — ทำ AWS Hands-on ได้เฉพาะขอบเขตที่ระบุในเอกสารนี้
- [ ] **LOCAL-ONLY** — ห้ามสร้าง AWS Resource และใช้ Local Simulation แทน

**เหตุผลประกอบคำตัดสิน:**  
**ผู้เรียนยืนยันก่อนสร้าง Resource:** [ ]  
**วันที่ยืนยัน:**  

## Checklist หลัง AWS Lab

- [ ] Terminate EC2 แล้ว ไม่ใช่เพียง Stop
- [ ] ลบ EBS Volume/Snapshot ที่ไม่ต้องใช้
- [ ] Release Elastic IP และตรวจ Public IPv4 ที่ค้าง
- [ ] ตรวจ Resource ในทุก Region ที่เคยใช้
- [ ] ตรวจ Billing และ Credit Balance หลัง Lab
- [ ] บันทึกค่าใช้จ่ายจริงใน `docs/learning-log.md`
- [ ] ยืนยันค่าใช้จ่ายจริงเป็น 0 บาท
- [ ] ยืนยันไม่มี Resource ค้าง

## แหล่งข้อมูลที่ต้องตรวจใหม่เมื่อเริ่ม Phase 11

- [AWS Free Tier](https://aws.amazon.com/free/)
- [AWS Free Tier plans](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier-plans.html)
- [Tracking Free Tier usage](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/tracking-free-tier-usage.html)
- [Amazon VPC pricing](https://aws.amazon.com/vpc/pricing/)
- [Amazon EC2 pricing](https://aws.amazon.com/ec2/pricing/on-demand/)
