import time
import simulator
import database

print("Sistem başlatıldı... veri gönderiliyor")

while True:
    sicaklik, basinc, uretim = simulator.generate_data()

    database.insert_sensor_data(sicaklik, basinc, uretim)

    print("SQL'e gönderildi:", sicaklik, basinc, uretim)

    time.sleep(1)