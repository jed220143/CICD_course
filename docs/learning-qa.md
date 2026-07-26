# Learning Q&A Notes

ไฟล์นี้ใช้จดคำถามยิบย่อยระหว่างเรียนแบบสั้น ๆ เพื่อย้อนอ่านทีหลัง

## Docker / Compose / Volume

### Dockerfile กับ Docker Compose ต่างกันยังไง?

Dockerfile คือสูตรสร้าง image ของ service เดียว ส่วน Compose คือไฟล์รวมระบบหลาย container ให้รันร่วมกัน พร้อม network, volume, ports และ environment

### ทุก container ต้องมี Dockerfile ไหม?

ไม่ต้อง มีเฉพาะ service ที่เรา build เอง เช่น `api` และ `simulator` ส่วน `postgres`, `nginx`, `mosquitto` ใช้ image สำเร็จรูปได้เลย

### `build.context` คืออะไร?

คือโฟลเดอร์ที่ Docker ใช้เป็นบริบทตอน build image เช่น `../../api` หมายถึงไปอ่าน Dockerfile และไฟล์ในโฟลเดอร์ `api`

### `image: mini-telemetry-api:dev` คือเอา image ขึ้น GitHub แล้วไหม?

ยังไม่ใช่ ตอนนี้คือชื่อ image local ในเครื่องหรือใน CI runner ถ้าจะขึ้น GitHub Container Registry ต้องมีขั้น `docker push` เพิ่ม

### Volume คือ DB ไหม?

Volume ไม่ใช่ DB แต่เป็นพื้นที่เก็บข้อมูลถาวรที่ DB ใช้ ถ้าลบ container แต่ไม่ลบ volume ข้อมูล DB ยังอยู่

### Migration files อยู่ใน volume ไหม?

ไม่อยู่ ไฟล์ migration อยู่ใน Git ส่วนผลลัพธ์หลังรัน migration เช่น tables, schema, rows และ `alembic_version` อยู่ใน PostgreSQL ซึ่งเก็บใน volume

## Database / SQLAlchemy / Alembic

### SQLAlchemy คืออะไร?

คือ library ให้ Python คุยกับ DB และนิยาม table/model ด้วย code

### Alembic คืออะไร?

คือเครื่องมือจัดการประวัติการเปลี่ยน schema ของ DB เช่น create table, add column, create index

### Production ต้องเข้าไปพิมพ์ SQL สร้างตารางเองไหม?

ปกติไม่ควร แก้ schema ผ่าน Alembic migration ที่อยู่ใน Git แล้ว deploy ด้วย `alembic upgrade head`

### `0001`, `0002` migration คือประวัติการสร้างไหม?

ใช่ เป็นลำดับการเปลี่ยน schema เพื่อให้คนอ่านง่าย แต่ Alembic รู้ลำดับจริงจาก `revision` และ `down_revision` ข้างในไฟล์

### Deploy รู้ได้ไงว่าต้องรัน migration ไหนก่อน?

Alembic ดู table `alembic_version` ใน DB ว่ารันถึง revision ไหนแล้ว จากนั้นรัน migration ถัดไปจนถึง `head`

## GitHub Actions / CI

### GitHub Actions คืออะไร?

คือระบบ automation ของ GitHub ที่รัน workflow เมื่อมี event เช่น push หรือ pull request

### Runner คืออะไร?

Runner คือเครื่องชั่วคราวที่ GitHub เตรียมให้รัน job คล้าย VM ชั่วคราว พอ job จบเครื่องก็ถูกทิ้ง

### GitHub รู้ได้ไงว่าต้องใช้ VM แบบไหน?

ดูจาก `runs-on` ใน workflow เช่น `ubuntu-latest` หรือ `ubuntu-24.04`

### GitHub Actions ฟรีไหม?

Public repo ใช้ standard GitHub-hosted runners ฟรี ส่วน private repo มี free minutes ตาม plan เช่น GitHub Free มี quota รายเดือน

### ทำไม CI build image ได้ทั้งที่ยังไม่ push image?

เพราะ CI build จาก source code + Dockerfile บน runner ชั่วคราว เพื่อเช็กว่า build ผ่าน แต่ image จะหายหลัง job จบถ้าไม่ push ไป registry

### ทำไมอนาคตต้อง push image ไป registry?

เพราะตอน deploy จริง server ต้องมีที่ดึง image เวอร์ชันที่ผ่าน CI แล้ว เช่น GHCR, Docker Hub หรือ ECR

### ทำไมไม่ push image ทุก feature branch?

เพราะ registry จะรกและเสี่ยงใช้ image ที่ยังไม่ผ่าน review ใน production เราจึง build ตรวจทุก PR แต่ push image เฉพาะ main, version tag หรือ manual run

### CD ต่างจาก CI ยังไง?

CI ตรวจว่า test/build ผ่าน ส่วน CD เอาสิ่งที่ผ่านแล้วไปรันจริง โดยต้องมีขั้น migrate, start/restart service และ health check

### ทำไมต้องเอา Alembic migration เข้า API image?

เพราะตอน deploy จริงควรรัน migration จาก image เดียวกับ code ที่กำลัง deploy ไม่ควรพึ่งไฟล์หรือ venv บนเครื่อง deploy แบบ manual

### ทำไม deploy script ต้องเช็ก exit code ของ `docker compose`?

เพราะ PowerShell ไม่ได้ throw error ให้ทุก native command อัตโนมัติ ถ้าไม่เช็ก `$LASTEXITCODE` script อาจรันต่อและ health check ของ container เก่าหลอกว่า deploy สำเร็จ

### Rollback ใน deploy script คือ rollback ทุกอย่างไหม?

ยังไม่ใช่ ตอนนี้ rollback เฉพาะ application image คือ API และ simulator ส่วน DB schema ไม่ downgrade อัตโนมัติ เพราะเสี่ยงข้อมูลหาย ต้องออกแบบ migration strategy แยกต่างหาก

### Git tag ใช้ทำอะไรใน CI/CD?

Git tag ใช้ mark commit เป็น release เช่น `v0.2.0` และใช้ trigger workflow ให้ build/push image versioned tag ที่อ้างอิง release นั้นได้

### Deploy จาก registry ต่างจาก deploy-local เดิมยังไง?

deploy-local เดิม build image จาก source บนเครื่องเรา ส่วน deploy จาก registry จะ `docker pull` image ที่ CI/CD publish แล้วมารัน เหมือน production มากกว่า

### `unauthorized` ตอน pull GHCR แปลว่าอะไร?

แปลว่า Docker ยังไม่มีสิทธิ์อ่าน package นั้น อาจเพราะ image ยังไม่ได้ publish, package เป็น private, หรือยังไม่ได้ `docker login ghcr.io`

### ทำไมเปลี่ยน package visibility แล้ว pull ได้?

เพราะ GHCR package ถูกทำให้ public/readable แล้ว Docker จึง pull image ได้โดยไม่ต้อง login ด้วย token

### ทำไมย้าย ports ของ DB/API/Broker ออกจาก compose หลัก?

เพราะ production ไม่ควรเปิด service ภายในออก host ถ้าไม่จำเป็น ให้ traffic เข้าทาง NGINX แล้วคุยกันผ่าน Docker network ภายใน

### `compose.local.yaml` คืออะไร?

คือ override สำหรับ dev/debug เช่นเปิด DB port ให้เครื่องเรา query ได้ หรือ bind mount `local-artifacts/` เพื่อดูไฟล์ runtime โดยไม่ปนกับ deploy config หลัก

### ทำไมเคยมี Compose 4 ไฟล์ แล้วแก้เหลือ 2?

ไฟล์ `compose.registry.yaml` และ `compose.aws.yaml` คัดลอกโครงสร้างระบบเกือบทั้งหมด ทำให้เสี่ยงแก้ไม่ครบและเข้าใจยาก จึงรวม release/AWS ไว้ใน `compose.yaml` แล้วใช้ environment เลือก image tag และ secret ส่วน `compose.local.yaml` มีเฉพาะ build, debug ports และ bind mount สำหรับ Local

## NGINX / Config / Production-minded

### NGINX config ขึ้น Git ปลอดภัยไหม?

ปลอดภัยถ้าไม่มี secret เช่น password, token, private key; config routing เช่น `proxy_pass http://api:8000/` ควรอยู่ใน Git ได้

### ทำไมแยก production-like compose กับ local-only override?

เพื่อกันของ dev เช่น debug ports, bind mount, local artifacts หลุดไป production แต่เราตกลงว่าจะยังไม่ทำตอนนี้ รอถึงบท deploy/production hardening

### `local-artifacts/` คืออะไร?

คือไฟล์ runtime ที่ simulator เขียนออกมาบนเครื่องเพื่อให้ดูง่ายตอนเรียน ไม่ใช่ source code จึงถูก ignore ไม่ push

## Python Project Files

### `.toml` คืออะไร?

TOML คือรูปแบบไฟล์ config คล้าย JSON/YAML ในโปรเจกต์เราใช้ `pyproject.toml` บอกชื่อ project, Python version, dependencies และ pytest config

## AWS Account Safety

### ทำไมตอนตั้ง MFA ต้องกรอกรหัส 2 ชุด ทั้งที่แอปมีรหัสเดียว?

เป็นรหัสจาก Authenticator รายการเดียวกันแต่คนละรอบเวลา: กรอกรหัสปัจจุบันเป็น Code 1 รอประมาณ 30 วินาทีให้รหัสเปลี่ยน แล้วกรอกรหัสใหม่เป็น Code 2 เพื่อให้ AWS ตรวจว่าเวลาของอุปกรณ์ตรงและสร้างรหัสต่อเนื่องได้ถูกต้อง

### ทำไมต้องสร้าง IAM user ทั้งที่ Root ก็ใช้งานได้?

Root มีสิทธิ์ควบคุมทั้งบัญชีและควรใช้เฉพาะงานดูแลบัญชีที่จำเป็น ส่วนงานประจำให้ใช้ IAM user ที่ได้รับสิทธิ์เท่าที่งานต้องใช้ เพื่อลดความเสียหายหากรหัสผ่านหรือ session หลุด

### `not authorized to perform ec2:DescribeInstances` คืออะไร?

หมายถึง IAM user ยืนยันตัวตนและเข้า Console ได้แล้ว แต่ยังไม่มี policy ที่อนุญาตให้อ่านรายการ EC2 ในบทนี้ต้องตรวจว่า user อยู่ในกลุ่ม `cicd-lab` และกลุ่มมี `AmazonEC2FullAccess` จริง

### ไฟล์ `.pem` คืออะไร และใช้ตอนใด?

เป็นไฟล์ private key ฝั่งผู้ดูแลสำหรับพิสูจน์ตัวตนตอน SSH เข้า EC2 โดย public key คู่กันถูกใส่ไว้ในเครื่อง EC2 ตอนสร้าง instance จึงเข้าเครื่องได้โดยไม่ส่งรหัสผ่านผ่านเครือข่าย ห้ามแชร์หรือ commit `.pem` ลง Git

### `WARNING: UNPROTECTED PRIVATE KEY FILE` คืออะไร?

Windows พบว่าผู้ใช้อื่นมีสิทธิ์อ่าน private key จึงให้ SSH ปฏิเสธไฟล์เพื่อป้องกันการขโมยกุญแจ ต้องปิด inherited permissions และให้สิทธิ์อ่านเฉพาะ Windows user เจ้าของไฟล์ก่อนใช้

### SSH จากบ้านต้องใช้ Public IP หรือ Private IP ของ EC2?

ใช้ Public IPv4 หรือ Public DNS เพราะ Private IP เช่น `172.31.x.x` ใช้สื่อสารภายใน VPC และเครื่องที่บ้านเข้าถึงตรง ๆ ไม่ได้ Public IPv4 แบบ auto-assigned อาจเปลี่ยนหลัง Stop/Start จึงต้องตรวจ Console และแก้ SSH config ใหม่

### AWS Lab นี้ต้องสร้าง Gateway เองไหม?

ไม่ต้องสร้างเพิ่ม Default VPC มี Internet Gateway และ route สำหรับ public subnet อยู่แล้ว เราไม่ใช้ NAT Gateway เพราะไม่จำเป็นและมีค่าใช้จ่าย และไม่ใช้ API Gateway เพราะ NGINX container ทำหน้าที่รับ traffic และ reverse proxy ไป API ภายในระบบ

### AWS API Gateway จำเป็นเมื่อใด?

ใช้เมื่ออยากได้บริการกลางแบบ managed สำหรับเปิด API โดยไม่ดูแล reverse proxy เอง เช่น API ของ Lambda/serverless, การตรวจ API key/JWT, rate limit, quota, routing หลาย backend และเก็บ metrics กลาง ระบบปัจจุบันมี EC2 เครื่องเดียวและ NGINX ทำหน้าที่รับ API อยู่แล้วจึงยังไม่จำเป็น

### AWS Lambda เหมาะกับงานแบบใด?

เหมาะกับงาน event-driven ที่เริ่มเมื่อมี HTTP request, message, schedule หรือไฟล์ใหม่ ทำงานช่วงสั้นแล้วจบ และไม่ต้องดูแล server เอง เช่น webhook, resize รูป, scheduled cleanup และ API ขนาดเล็ก ไม่เหมาะกับ process ที่ต้องรันตลอดหรือเก็บ state ในเครื่อง เช่น MQTT subscriber ที่ต้องเชื่อมต่อค้างไว้
