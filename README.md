## الصفحة الثانية: البيضة تتشقق (Page 02)
[📥 اضغط هنا لتحميل ملف الكتاب بصيغة PDF](kdp_output/Tiko_and_the_Mysterious_Egg_Interior.pdf)

```python
import os
from PIL import Image, ImageDraw, ImageFont

# إعدادات المقاسات القياسية لـ KDP
DPI = 300
WIDTH_PX = int(8.625 * DPI)   # 2587 px
HEIGHT_PX = int(11.25 * DPI)  # 3375 px

# إنشاء الصفحة الثانية
canvas = Image.new("L", (WIDTH_PX, HEIGHT_PX), 255)
draw = ImageDraw.Draw(canvas)

# حفظ الصفحة
os.makedirs("raw_images", exist_ok=True)
canvas.save("raw_images/page_02.png", dpi=(DPI, DPI))
print("Page 02 saved successfully!")
```
