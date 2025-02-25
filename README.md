# 🌌 ESP32 Sensor DHT11 dengan OLED, Ubidots & Flask

Proyek ini menggunakan **ESP32** untuk membaca motion dari **sensor PIR** serta suhu dan kelembapan dari **sensor DHT11**, menampilkannya di **layar OLED**, serta mengirim data ke **Ubidots** melalui WiFi. Data yang dikirim juga akan disimpan di **MongoDB** menggunakan **Flask**.

---

## 📌 **Fitur**
- ✅ Menghubungkan ESP32 ke WiFi.
- ✅ Membaca data suhu & kelembapan dari **DHT11**.
- ✅ Menampilkan data di **OLED SSD1306**.
- ✅ Mengirim data ke **Ubidots**.
- ✅ Menyimpan data ke **MongoDB** melalui Flask.
- ✅ Menyalakan LED merah jika terdeteksi gerakan di **PIR**.
- ✅ API Flask untuk mengambil dan menganalisis data sensor.

![Rangkaian ESP32-DHT11-PIR](https://github.com/user-attachments/assets/e1e268e6-d496-4aa8-952e-1fc68b0dacd8)
![Dashboard Ubidots UNI249-Innovatrix SIC BATCH 6](https://github.com/user-attachments/assets/a49c1786-df16-4eeb-8ddf-caaf5b3d9980)

---

## 🛂 **Persyaratan**
### 🛠 **Hardware**
- ESP32
- Sensor DHT11
- Layar OLED SSD1306 (I2C)
- LED merah & resistor
- Kabel jumper
- Sensor PIR

### 🌟 **Software & Library**
#### 💻 **Di ESP32**
- machine → Mengontrol pin ESP32
- network → Menghubungkan ke WiFi
- urequests → Mengirim data ke Ubidots
- ssd1306 → Menampilkan teks di OLED
- dht → Membaca sensor DHT11
- ujson → Format data JSON
- time → Delay antar pengukuran

#### 🌐 **Di Server Flask**
- Flask → Framework web untuk API
- pymongo → Menghubungkan Flask ke MongoDB
- datetime → Menangani waktu dengan konversi ke WIB

---

## 🚀 **Instalasi & Penggunaan**

### 1️⃣ **Kloning atau Unduh Kode**
```sh
git clone https://github.com/ultra-dot/SIC6-Innovatrix.git
```

### 2️⃣ **Tambahkan File config.py**
Buat file config.py untuk menyimpan konfigurasi WiFi & Ubidots:
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

### 4️⃣ **Menjalankan Flask API**
1. Install dependensi:
```sh
pip install flask pymongo
```
2. Jalankan Flask:
```sh
python flask_app.py
```

API yang tersedia:
- **POST /sensor1/data** → Menyimpan data sensor ke MongoDB.
- **GET /sensor1/data** → Mengambil semua data sensor.
- **GET /sensor1/temperature/avg** → Menghitung rata-rata suhu.
- **GET /sensor1/kelembapan/avg** → Menghitung rata-rata kelembapan.
- **GET /sensor1/motion/count** → Menghitung jumlah deteksi gerakan.

### 5️⃣ **Jalankan Program ESP32**
ESP32 akan:
1. Terhubung ke WiFi
2. Membaca suhu & kelembapan dari DHT11
3. Menampilkan data di OLED
4. Mengirim data ke Ubidots
5. Menyimpan data ke MongoDB melalui Flask
6. Menyalakan LED merah jika suhu > 31°C

---

## 📊 **Dashboard Ubidots & Flask API**
1. Masuk ke [Ubidots](https://industrial.ubidots.com/).
2. Buat **Device** baru dengan nama esp32.
3. Lihat data suhu & kelembapan yang dikirim dari ESP32.
4. Gunakan **Postman** atau browser untuk mengakses API Flask.

---

## 🔧 **Troubleshooting**
- **WiFi tidak terhubung?** Pastikan SSID & Password benar di config.py.
- **OLED tidak menampilkan teks?** Periksa koneksi I2C (SDA ke 21, SCL ke 22).
- **Data tidak terkirim ke Ubidots?** Cek apakah Token API valid.
- **Flask tidak menerima data?** Pastikan ESP32 mengirim ke alamat Flask API yang benar.

---

## 📚 **Copyright**
Proyek ini dibuat oleh Innovatrix IPB University. Bebas digunakan & dimodifikasi! 😊
