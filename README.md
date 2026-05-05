# factory-data-system  
# Gerçek Zamanlı Sensör Veri Sistemi (Python + MSSQL + REST API)

Bu proje, fabrikadaki sensör verilerini simüle eden ve bu verileri Microsoft SQL Server veritabanına kaydeden ve REST API üzerinden erişilebilir hale getiren bir backend sistemidir.

* Dashboard henüz geliştirme aşamasındadır. Bu repo şu anda sadece veri üretimi, veritabanı ve API katmanını içerir.

---

#  Önemli Güncelleme (CSV → MSSQL)

Eski sistem:
- Veriler CSV dosyasına yazılıyordu
- Dosya üzerinden veri okunuyordu

Yeni sistem:
- CSV kullanımı kaldırıldı 
- Veriler doğrudan MSSQL veritabanına yazılıyor ✔
- Verilere REST API üzerinden erişiliyor ✔
- Sistem artık gerçek backend mimarisine uygun hale getirildi ✔

CSV dosyası sadece eski sürüm referansı olarak repoda bulunabilir.

---

#  Proje Yapısı

factory-data-system/
│
├── src/
│   ├── main.py        # Sensör verisi üretir ve DB’ye gönderir
│   ├── database.py    # MSSQL bağlantısı ve veri işlemleri
│   ├──api.py          # REST API servisi
│   ├── requirements.txt
│   └── README.md
│
└── archive/
    ├──sensor_simulator.py    # Eski Script tek dosyada çalışır
    └──sensor_data.csv        # Değerler buraya yazılır

---

#  Kullanılan Teknolojiler

- Python
- Microsoft SQL Server
- FastAPI
- Uvicorn
- pyodbc

---

#  Veritabanı Kurulumu

SQL Server Management Studio’da aşağıdaki dosya çalıştırılır:

database_setup.sql

Bu işlem:
- FactoryDB veritabanını oluşturur
- SensorData tablosunu oluşturur

---

#  Veritabanı Bağlantısı

database.py dosyasında şu bilgileri düzenle:

SERVER = "YOUR_SERVER"
DATABASE = "FactoryDB"
USERNAME = "YOUR_USERNAME"
PASSWORD = "YOUR_PASSWORD"

---

#  Kurulum

pip install -r requirements.txt

---

# ▶ Sensör Simülasyonunu Çalıştırma

cd src
python main.py

Bu işlem:
- Rastgele sensör verisi üretir
- Verileri MSSQL veritabanına kaydeder

---

#  API’yi Çalıştırma

cd src
uvicorn api:app --reload

Sunucu çalışınca:

http://127.0.0.1:8000

---

#  API Dokümantasyonu

Swagger UI:

http://127.0.0.1:8000/docs

---

#  API Endpointleri

GET /sensor

Bu endpoint:
- MSSQL’den son sensör verilerini çeker
- JSON formatında döndürür

---

#  Sistem Çalışma Mantığı

1. Python sensör verisi üretir (sıcaklık, basınç, üretim)
2. Veriler MSSQL veritabanına kaydedilir
3. FastAPI bu verileri API üzerinden sunar
4. İleride dashboard bu API’den veri çekecektir

---

#  Proje Amacı

- Python ile veri üretimi simülasyonu
- MSSQL veritabanı kullanımı
- REST API geliştirme
- Gerçek backend sistem mimarisini öğrenmek