# AWS Free Tier Gate — ห้ามสร้าง Resource ก่อนผ่าน

เอกสารนี้เป็น Safety Gate สำหรับ AWS Hands-on ของ Mini Telemetry Platform เป้าหมายคือ **ค่าใช้จ่ายจริง 0 บาท**

> หากตรวจข้อใดไม่ได้หรือสถานะไม่ชัดเจน ให้เลือก `LOCAL-ONLY` ทันที ห้ามเดาและห้าม Upgrade เป็น Paid plan

## ข้อมูลตรวจสอบ

ห้ามบันทึก Account ID, Card, Access Key, Secret Key หรือข้อมูลลับในไฟล์นี้

| รายการ | ค่าที่ตรวจพบ |
|---|---|
| วันที่ตรวจ | 2026-07-26 (ตรวจซ้ำก่อนเริ่ม EC2 Lab) |
| วันที่สร้างบัญชีโดยประมาณ | 2026-07-13 |
| Plan ที่เลือกตอนสมัคร | Free account plan |
| Credit คงเหลือ | USD 100.00; ใช้แล้ว USD 0.00 |
| วันหมดอายุ Credit | 2027-07-13 |
| วันหมดอายุ Free plan | ประมาณ 2027-01-13 (6 เดือน); ต้องยืนยันวันที่จริงจาก Billing Console |
| Region สำหรับ Lab | Asia Pacific (Singapore) `ap-southeast-1` |
| ระยะเวลา EC2 Lab ที่วางแผน | ไม่เกิน 3 ชั่วโมงต่อรอบ แล้ว Terminate |
| ค่าใช้จ่ายประมาณการก่อนใช้ Credit | ไม่เกิน USD 1 ต่อรอบสำหรับ EC2 + EBS + Public IPv4; ค่าเรียกเก็บจริง 0 บน Free account plan |

## Gate A — Account Safety

สถานะปัจจุบัน: **PASS สำหรับ EC2 Lab ที่ระบุเท่านั้น**

- [x] Billing Console แสดงว่าเป็น **Free account plan**
- [x] Console ระบุว่าจะไม่เกิดค่าใช้จ่ายจนกว่าจะ Upgrade
- [x] ยังไม่หมดระยะ Free plan และ Credit
- [x] Credit คงเหลือ USD 100.00 และใช้แล้ว USD 0.00 ณ วันที่ตรวจ
- [x] บัญชียังคงเป็น Free account plan จึงไม่ได้เข้าร่วม AWS Organizations
- [x] จะไม่ Upgrade เป็น Paid plan ระหว่างหลักสูตร
- [x] Root เปิด MFA แล้ว (ผู้เรียนยืนยันวันที่ 2026-07-25)
- [x] สร้าง IAM user `cicd-learner`, เปิด MFA และทดสอบ Console login แล้ว (ไม่ใช้ Root ทำงานประจำ)
- [x] เปิด Free Tier Usage Alert แล้ว (ยืนยันจาก Billing preferences วันที่ 2026-07-25)
- [x] ไม่ใช้ Zero-spend Budget ตามการตัดสินใจของผู้เรียน; บัญชีเป็น Free account plan และจะตรวจ Billing/Credits ก่อน–หลัง Lab แทน

## Gate B — Resource Safety

- [x] ตรวจสิทธิ์ Free Tier ปัจจุบันของ EC2, EBS และเงื่อนไข Free account plan แล้ว
- [x] ใช้เฉพาะ Service/Feature ที่ Free account plan อนุญาต
- [x] ไม่ใช้ NAT Gateway, RDS, EKS, Load Balancer หรือ Marketplace
- [x] ใช้ข้อมูลจำลอง ไม่มีข้อมูลจริงหรือ Secret ผ่าน Public HTTP
- [x] SSH และพอร์ต Lab จำกัด Source IP ของผู้เรียน
- [x] กำหนดเวลาจบ Lab ไม่เกิน 3 ชั่วโมงต่อรอบ
- [x] มีคำสั่ง/ขั้นตอน Health Check และ Rollback
- [x] มี Destroy Checklist ครอบคลุม EC2, EBS, Snapshot และ Public/Elastic IP
- [x] Source และ image เก็บใน GitHub/GHCR แล้ว ไม่พึ่ง EC2 เป็นที่เก็บถาวร

## คำตัดสิน

- [x] **PASS** — ทำ AWS Hands-on ได้เฉพาะขอบเขตที่ระบุในเอกสารนี้
- [ ] **LOCAL-ONLY** — ห้ามสร้าง AWS Resource และใช้ Local Simulation แทน

**เหตุผลประกอบคำตัดสิน:** Free account plan, เครดิตเพียงพอ, MFA/สิทธิ์ผ่าน, EC2/EBS ที่เลือกมีป้าย Free tier eligible และจำกัด network จาก My IP
**ผู้เรียนยืนยันก่อนสร้าง Resource:** [x]
**วันที่ยืนยัน:** 2026-07-26

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
