#Setting Wifi & Ubidots

WIFI_SSID = "<SSID>"
WIFI_PASSWORD = "<PASSWORD>"
DEVICE_ID = "esp32"
TOKEN = "<Token Ubidots>"

UBIDOTS_URL = f"http://industrial.api.ubidots.com/api/v1.6/devices/{DEVICE_ID}"
HEADERS = {
    "Content-Type": "application/json",
    "X-Auth-Token": TOKEN
}
