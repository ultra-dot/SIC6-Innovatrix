from machine import Pin, I2C
import ujson
import network
import ssd1306
import urequests
from time import sleep
from dht import DHT11
import config  # Import konfigurasi dari config.py

# Inisialisasi sensor DHT11
DHT_PIN = Pin(4)
dht_sensor = DHT11(DHT_PIN)

# Inisialisasi sensor PIR
PIR_PIN = Pin(5, Pin.IN)

# Inisialisasi OLED
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Inisialisasi LED
LED_MOTION = Pin(18, Pin.OUT)

def connect_wifi():
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.connect(config.WIFI_SSID, config.WIFI_PASSWORD)
    print("Connecting to WiFi...")
    while not wifi.isconnected():
        sleep(1)
        print("Connecting...")
    print("WiFi Connected!", wifi.ifconfig())

def send_data(temp, humidity, motion):
    """Mengirim data ke Ubidots"""
    data = ujson.dumps({"temp": temp, "humidity": humidity, "motion": motion})
    try:
        print("Mengirim data ke server...")
        response = urequests.post(config.UBIDOTS_URL, headers=config.HEADERS, data=data)
        print("Response:", response.text)
        response.close()
    except Exception as e:
        print("[ERROR] Gagal mengirim data:", e)

def display_oled(temp, humidity, motion):
    """Menampilkan data pada OLED"""
    oled.fill(0)
    oled.text("Suhu: {}C".format(temp), 10, 10)
    oled.text("Kelembapan: {}%".format(humidity), 10, 30)
    oled.text("Gerakan: {}".format("Yes" if motion else "No"), 10, 50)
    oled.show()

# Mulai program
connect_wifi()

oled.fill(0)
oled.text("Innovatrix", 10, 20)
oled.text("IPB University", 10, 40)
oled.show()
sleep(3)

oled.fill(0)
oled.text("Mendeteksi...", 8, 26)
oled.show()
sleep(2)

# Debugging: Pastikan loop berjalan terus
counter = 0

while True:
    try:
        counter += 1
        print("Data ke-", counter)

        dht_sensor.measure()
        suhu = dht_sensor.temperature()
        kelembapan = dht_sensor.humidity()
        motion_detected = PIR_PIN.value()
        
        if motion_detected:
            LED_MOTION.value(1)
            
        else:
            LED_MOTION.value(0)


        print("Suhu: {}°C, Kelembapan: {}%, Gerakan: {}".format(
            suhu, kelembapan, "Yes" if motion_detected else "No"))

        display_oled(suhu, kelembapan, motion_detected)

        send_data(suhu, kelembapan, motion_detected)

    except Exception as e:
        print("[ERROR] Terjadi kesalahan:", e)
    
    
    # Delay 2 detik agar lebih jelas di log
    sleep(1)
