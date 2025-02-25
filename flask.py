from flask import Flask, jsonify, request
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId 
from datetime import datetime

app = Flask(__name__)

# Konfigurasi MongoDB
uri = "mongodb+srv://yoalsb:5CWuaFUUPnD34BMv@innovatrix.uh6xi.mongodb.net/?retryWrites=true&w=majority&appName=Innovatrix"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["innoDB"]
collection = db["sensor_data"]

# Fungsi untuk menghitung rata-rata
def calculate_avg(field):
    data = list(collection.find({}, {field: 1, "_id": 0}))
    values = [item[field] for item in data if field in item]
    return sum(values) / len(values) if values else 0

@app.route("/sensor1/temperature/avg", methods=["GET"])
def get_avg_temperature():
    avg_temp = calculate_avg("temperature")
    return jsonify({"average_temperature": avg_temp})

@app.route("/sensor1/kelembapan/avg", methods=["GET"])
def get_avg_humidity():
    avg_humidity = calculate_avg("humidity")
    return jsonify({"average_humidity": avg_humidity})

@app.route("/sensor1/motion/count", methods=["GET"])
def get_motion_count():
    motion_count = collection.count_documents({"motion": 1})
    return jsonify({"motion_detected_count": motion_count})

@app.route("/sensor1/data", methods=["POST"])
def receive_sensor_data():
    try:
        data = request.json
        if data:
            data["timestamp"] = datetime.utcnow()  # Tambahkan timestamp UTC
            collection.insert_one(data)
            return jsonify({"message": "Data berhasil disimpan", "data": data}), 201
        else:
            return jsonify({"error": "Data kosong"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/sensor1/data", methods=["GET"])
def get_all_sensor_data():
    try:
        data = list(collection.find())  
        for item in data:
            item["_id"] = str(item["_id"])  # Konversi ObjectId ke string
            item["timestamp"] = item["timestamp"].isoformat() if "timestamp" in item else None  # Format timestamp
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
