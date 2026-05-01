import csv
import random
import time
import pyodbc

conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=BOZKURT;"
    "DATABASE=FactoryDB;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

with open("sensor_data.csv","w",newline="") as deger:
    writer = csv.writer(deger)
    writer.writerow(["sicaklik","basinc","uretim"])

while True:
    sicaklik = round(random.uniform(20,80),2)
    basinc   = round(random.uniform(1,10),2)
    uretim   = random.randint(0,20)

    # CSV
    with open("sensor_data.csv","a",newline="") as deger:
        writer = csv.writer(deger)
        writer.writerow([sicaklik, basinc, uretim])

    # MSSQL
    cursor.execute("""
        INSERT INTO SensorData (temperature, pressure, production)
        VALUES (?, ?, ?)
    """, (sicaklik, basinc, uretim))

    conn.commit()

    print("SQL'e gönderildi:", sicaklik, basinc, uretim)

    time.sleep(1)