from machine import Pin, I2C
import ujson
import network
import ssd1306
import urequests  # Gunakan urequests, bukan requests
from time import sleep
from dht import DHT11

# Konfigurasi WiFi dan Ubidots
DEVICE_ID = "esp32"
WIFI_SSID = "AB"
WIFI_PASSWORD = "alifbaha"
TOKEN = "BBUS-rgoQlc7iA8Wvipx54JMvBx4pfV7bRw"
UBIDOTS_URL = f"http://industrial.api.ubidots.com/api/v1.6/devices/{DEVICE_ID}"
HEADERS = {
    "Content-Type": "application/json",
    "X-Auth-Token": TOKEN
}

# Inisialisasi sensor DHT11 dan LED
DHT_PIN = Pin(4)
dht_sensor = DHT11(DHT_PIN)
LED_RED = Pin(5, Pin.OUT)

# Inisialisasi OLED
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

def connect_wifi():
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.connect(WIFI_SSID, WIFI_PASSWORD)
    print("Connecting to WiFi...")
    while not wifi.isconnected():
        sleep(0.5)
        print("Connecting...")
    print("WiFi Connected!", wifi.ifconfig())

def send_data(temp, humidity):
    data = ujson.dumps({"temp": temp, "humidity": humidity})
    try:
        response = urequests.post(UBIDOTS_URL, headers=HEADERS, data=data)
        print("Data Sent! Response:", response.text)
        response.close()
    except Exception as e:
        print("Failed to send data:", e)

def display_oled(temp, humidity):
    oled.fill(0)
    oled.text("Suhu: {}C".format(temp), 10, 20)
    oled.text("Kelembapan: {}%".format(humidity), 10, 40)
    oled.show()

def control_led(temp):
    LED_RED.value(1 if temp > 31 else 0)

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

while True:
    try:
        dht_sensor.measure()
        suhu = dht_sensor.temperature()
        kelembapan = dht_sensor.humidity()
        
        print("Suhu: {}°C, Kelembapan: {}%".format(suhu, kelembapan))
        display_oled(suhu, kelembapan)
        control_led(suhu)
        send_data(suhu, kelembapan)
        
    except Exception as e:
        print("Error reading sensor:", e)
    
    sleep(5)
