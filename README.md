# 📡 ESP32 Sensor DHT11 dengan OLED & Ubidots

Proyek ini menggunakan **ESP32** untuk membaca suhu dan kelembapan dari **sensor DHT11**, menampilkannya di **layar OLED**, serta mengirim data ke **Ubidots** melalui WiFi. Jika suhu melebihi 31°C, LED merah akan menyala sebagai indikator.

---

## 📌 **Fitur**
- ✅ Menghubungkan ESP32 ke WiFi.
- ✅ Membaca data suhu & kelembapan dari **DHT11**.
- ✅ Menampilkan data di **OLED SSD1306**.
- ✅ Mengirim data ke **Ubidots**.
- ✅ Menyalakan LED merah jika suhu > 31°C.

---

## 📦 **Persyaratan**
### 🛠 **Hardware**
- ESP32
- Sensor DHT11
- Layar OLED SSD1306 (I2C)
- LED merah & resistor
- Kabel jumper

### 📜 **Library yang Digunakan**
- `machine` → Mengontrol pin ESP32
- `network` → Menghubungkan ke WiFi
- `urequests` → Mengirim data ke Ubidots
- `ssd1306` → Menampilkan teks di OLED
- `dht` → Membaca sensor DHT11
- `ujson` → Format data JSON
- `time` → Delay antar pengukuran

---

## 🚀 **Instalasi & Penggunaan**

### 1️⃣ **Kloning atau Unduh Kode**
```sh
# Clone repositori
git clone https://github.com/ultra-dot/SIC6-Innovatrix.git
```

### 2️⃣ **Tambahkan File `config.py`**
Buat file `config.py` untuk menyimpan konfigurasi WiFi & Ubidots:
```python
# config.py
WIFI_SSID = "<SSID>"
WIFI_PASSWORD = "<PASSWORD>"
DEVICE_ID = "esp32"
TOKEN = "<TOKEN UBIDOTS>"

UBIDOTS_URL = f"http://industrial.api.ubidots.com/api/v1.6/devices/{DEVICE_ID}"
HEADERS = {
    "Content-Type": "application/json",
    "X-Auth-Token": TOKEN
}
```

### 3️⃣ **Upload Kode ke ESP32**
Gunakan **Thonny**, **uPyCraft**, atau **ampy** untuk mengunggah kode ke ESP32.

```sh
# Jika menggunakan ampy
ampy --port /dev/ttyUSB0 put main.py
ampy --port /dev/ttyUSB0 put config.py
```

### 4️⃣ **Jalankan Program**
ESP32 akan:
1. Terhubung ke WiFi
2. Membaca suhu & kelembapan dari DHT11
3. Menampilkan data di OLED
4. Mengirim data ke Ubidots
5. Menyalakan LED merah jika suhu > 31°C

---

## 📊 **Dashboard Ubidots**
1. Masuk ke [Ubidots](https://industrial.ubidots.com/).
2. Buat **Device** baru dengan nama `esp32`.
3. Lihat data suhu & kelembapan yang dikirim dari ESP32.

---

## 🔧 **Troubleshooting**
- **WiFi tidak terhubung?** Pastikan SSID & Password benar di `config.py`.
- **OLED tidak menampilkan teks?** Periksa koneksi I2C (SDA ke 21, SCL ke 22).
- **Data tidak terkirim ke Ubidots?** Cek apakah Token API valid.

---

## 📜 **Lisensi**
Proyek ini menggunakan lisensi **MIT**. Bebas digunakan & dimodifikasi! 😊

