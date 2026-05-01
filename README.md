# factory-data-system
# Gerçek Zamanlı Sensör Veri Sistemi

## Proje Açıklaması
Bu proje, Python kullanarak sahte sensör verisi üretir ve bu verileri her saniye Microsoft SQL Server veritabanına kaydeder. Ayrıca veriler CSV dosyasına da yazılır.

---

## Kullanılan Teknolojiler
- Python
- Microsoft SQL Server
- pyodbc kütüphanesi
- CSV dosya sistemi

---

## Proje Nasıl Çalışır?

1. Python sürekli olarak rastgele sensör verisi üretir (sıcaklık, basınç, üretim)
2. Bu veriler her 1 saniyede bir güncellenir
3. Veriler hem CSV dosyasına hem de SQL Server veritabanına yazılır
4. SQL Server’da tablo içinde saklanır ve sorgulanabilir

---

## Veritabanı Kurulumu

1. SQL Server Management Studio açılır
2. database_setup.sql dosyası çalıştırılır
3. FactoryDB veritabanı ve SensorData tablosu oluşturulur

---

## Çalıştırma

1. Gerekli kütüphane kurulumu:
   pip install pyodbc

2. Python dosyasını çalıştır:
   python sensor_to_mssql.py

---

## Proje Amacı
Gerçek zamanlı veri akış sistemlerini öğrenmek, Python ile veritabanı bağlantısını anlamak ve basit IoT simülasyonu oluşturmak.