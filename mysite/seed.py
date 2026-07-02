import os
import sys
import django

# Set up Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from mysite.vc.models import Category, Product

def seed_db():
    print("Clearing existing data...")
    Product.objects.all().delete()
    Category.objects.all().delete()

    print("Creating categories...")
    electronics = Category.objects.create(name="Electronics")
    accessories = Category.objects.create(name="Accessories")
    furniture = Category.objects.create(name="Furniture")

    print("Creating products...")
    
    # 1. Wireless Gaming Headphones
    Product.objects.create(
        name="Wireless Gaming Headphones (หูฟังเกมมิ่งไร้สาย ระบบเสียง 7.1)",
        description="สัมผัสประสบการณ์เสียงที่ยอดเยี่ยมกับหูฟังเกมมิ่งไร้สาย ระบบเสียงรอบทิศทาง 7.1 แบตเตอรี่ยาวนาน 30 ชั่วโมง สวมใส่สบายด้วยฟองน้ำเมมโมรี่โฟมที่นุ่มนวล พร้อมไฟ RGB สวยงามรอบตัวเครื่อง",
        price=1290.00,
        original_price=2590.00,
        image_url="/static/images/wireless_headphones.png",
        rating=4.80,
        sales_count=1420,
        stock=45,
        category=electronics,
        location="กรุงเทพมหานคร",
        is_featured=True
    )

    # 2. Premium Mechanical Keyboard
    Product.objects.create(
        name="Premium Mechanical Keyboard (คีย์บอร์ดกลไก Custom คีย์แคปสีส้ม-ดำ)",
        description="คีย์บอร์ดกลไกแบบ Custom คีย์แคป PBT ดับเบิ้ลช็อตสีส้ม-ดำ สวิตช์เสียงนุ่มนวล (Linear/Tactile) ตอบสนองรวดเร็ว เหมาะสำหรับการเล่นเกมและการทำงานระยะยาว รองรับการเชื่อมต่อแบบไร้สายและสายสัญญาณ",
        price=1890.00,
        original_price=3290.00,
        image_url="/static/images/mechanical_keyboard.png",
        rating=4.90,
        sales_count=850,
        stock=20,
        category=accessories,
        location="จังหวัดปทุมธานี",
        is_featured=True
    )

    # 3. Smart Watch AMOLED Display
    Product.objects.create(
        name="Smart Watch AMOLED Display (สมาร์ทวอทช์จอสีสันสดใส วัดสุขภาพ)",
        description="สมาร์ทวอทช์หน้าจอ AMOLED ขนาด 1.43 นิ้ว วัดอัตราการเต้นของหัวใจ ระดับออกซิเจนในเลือด (SpO2) ตัววัดการนอนหลับ โหมดออกกำลังกายมากกว่า 100 โหมด กันน้ำลึกระดับ 50 เมตร (5ATM) แบตเตอรี่ใช้ได้ยาวนาน 14 วันต่อการชาร์จ",
        price=990.00,
        original_price=1990.00,
        image_url="https://images.unsplash.com/photo-1546868871-7041f2a55e12?q=80&w=600&auto=format&fit=crop",
        rating=4.70,
        sales_count=2100,
        stock=150,
        category=electronics,
        location="กรุงเทพมหานคร",
        is_featured=False
    )

    # 4. Ergonomic Office Chair
    Product.objects.create(
        name="Ergonomic Office Chair (เก้าอี้เพื่อสุขภาพ รองรับหลังกระดูกสันหลัง)",
        description="เก้าอี้ทำงานเพื่อสุขภาพ ออกแบบตามหลักสรีรศาสตร์ (Ergonomics) พนักพิงผ้าตาข่ายระบายอากาศได้ดี โครงรองรับหลังส่วนล่าง (Lumbar Support) ปรับระดับที่วางแขน พนักพิงศีรษะ และความสูงเก้าอี้ได้ ช่วยลดอาการปวดเมื่อยสะสมจากการทำงานออฟฟิศ",
        price=3490.00,
        original_price=5990.00,
        image_url="https://images.unsplash.com/photo-1580481072645-022f9a6dbf27?q=80&w=600&auto=format&fit=crop",
        rating=4.60,
        sales_count=310,
        stock=12,
        category=furniture,
        location="จังหวัดนนทบุรี",
        is_featured=False
    )

    # 5. USB-C Hub 8-in-1
    Product.objects.create(
        name="USB-C Hub 8-in-1 Multiport Adapter (ตัวแปลงสายสัญญาณอเนกประสงค์)",
        description="ตัวแปลงสัญญาณสำหรับโน้ตบุ๊กและแท็บเล็ต พอร์ตเชื่อมต่อ 8 ช่อง ประกอบด้วย HDMI 4K @30Hz, USB 3.0 จำนวน 3 ช่อง, ช่องอ่าน SD/MicroSD Card, พอร์ต Ethernet (LAN) และพอร์ตชาร์จไฟแบบ USB-C Power Delivery รองรับ 100W",
        price=490.00,
        original_price=990.00,
        image_url="https://images.unsplash.com/photo-1468495244123-6c6c332eeece?q=80&w=600&auto=format&fit=crop",
        rating=4.50,
        sales_count=1890,
        stock=70,
        category=accessories,
        location="กรุงเทพมหานคร",
        is_featured=False
    )

    print("Database seeding completed successfully!")

if __name__ == '__main__':
    seed_db()
