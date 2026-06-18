# mysite2026
    242-19

## run server   
    uv run manage.py runserver 0.0.0.0:80
  
## http methods 
    GET > http://[IP_ADDRESS]/info
    POST
    PUT
    DELETE
    PATCH

## http status code
    200 OK > เรียบร้อย
    201 Created > เพิ่มข้อมูลสำเร็จ
    400 Bad Request > ส่งข้อมูลผิดพลาด
    401 Unauthorized > ไม่ได้รับอนุญาต
    403 Forbidden > ถูกห้าม
    404 Not Found > ไม่พบข้อมูล
    500 Internal Server Error > เกิดข้อผิดพลาดภายในเซิฟเวอร์

---

## URL Endpoints Implemented

| URL Path | HTTP Method | Response Format | Success Status | Description |
| :--- | :--- | :--- | :--- | :--- |
| `/` | `GET` | HTML | `200 OK` | หน้าต้อนรับ Django Default (รูปจรวด) |
| `/info` | `GET` | HTML | `200 OK` | แสดง IP เครื่องผู้ใช้งานและรายการ Request Headers |
| `/hello` | `GET` / `POST` | HTML | `200 OK` | หน้าฟอร์มกรอกชื่อ / ตอบกลับทักทาย "Hello, [Name]" |
| `/quiz/question` | `GET` | JSON | `200 OK` | ส่งคืนคำถามควิซ: `{"id": 1, "text": "ประเทศไทยมีกี่จังหวัด", "choices": [50, 68, 72, 77]}` |
| `/quiz/question/create` | `POST` | JSON | `200 OK` | รับและส่งข้อมูลกลับเป็น JSON คำถามที่ถูกสร้าง |