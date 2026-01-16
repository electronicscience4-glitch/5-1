from machine import Pin, I2C
import ssd1306
import time
import framebuf
# ڕێکخستنی I2C بۆ OLED
i2c = I2C(0, scl=Pin(1), sda=Pin(0))  # GPIO1=SCL, GPIO0=SDA
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

def display_message():
    """نیشاندانی نامە لەسەر OLED"""
    oled.fill(0)  # پاککردنەوەی شاشە
    oled.text("Sangar Mawaty", 0, 0) # ڕیزی یەکەم: ناوی تایبەت
    oled.text("Hello World!", 0, 16)  # ڕیزی دووەم: نامەی سەرەکی
    current_time = time.localtime()    # ڕیزی سێیەم: کاتی ڕۆژ
    time_str = "{:02d}:{:02d}:{:02d}".format(current_time[3], current_time[4], current_time[5])
    oled.text("Time: " + time_str, 0, 32)
    oled.text("System: Active", 0, 48)  # ڕیزی چوارەم: باری سیستەم
    oled.show()
def display_loading():
    """نیشاندانی شاشەی بارگە"""
    oled.fill(0)
    oled.text("Sangar Mawaty", 15, 10)
    oled.text("OLED System", 20, 25)
    oled.text("Loading...", 35, 40)
    oled.show()
def display_goodbye():
    """نیشاندانی شاشەی ماڵئاوایی"""
    oled.fill(0)
    oled.text("System Stopped", 10, 20)
    oled.text("Goodbye!", 40, 35)
    oled.show()

print("سیستەمی نیشاندانی OLED")
print("شاشەی 0.9 ئینج - I2C")

display_loading()
time.sleep(2)

counter = 0
try:
    while True:
        try:
            display_message()   # نیشاندانی نامە بەردەوام
            counter += 1             # زیادکردنی ژمارەی کاونتر بۆ نیشاندان
            print(f"Display update: {counter}")
            time.sleep(1)  # چاوەڕوانی 1 چرکە
            
        except Exception as e:
            oled.fill(0)
            oled.text("Error occurred", 0, 20)
            oled.text("Check system", 0, 35)
            oled.show()
            print(f"Error: {e}")
            time.sleep(2)
            
except KeyboardInterrupt:
    display_goodbye()
    print("سیستەم کۆتایی هات" )
