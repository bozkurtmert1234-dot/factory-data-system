from fastapi import FastAPI
import database

app = FastAPI()


# Test endpoint → API çalışıyor mu kontrol
@app.get("/")
def home():
    return {"mesaj": "Factory Data API çalışıyor"}


# Veritabanından son verileri getiren endpoint
@app.get("/sensor")
def get_sensor_data():

    rows = database.get_last_data()

    # pyodbc çıktısını JSON'a çevirmemiz gerekiyor
    result = []

    for row in rows:
        result.append({
            "id": row[0],
            "sicaklik": row[1],
            "basinc": row[2],
            "uretim": row[3],
            "tarih": str(row[4])
        })

    return {"veriler": result}