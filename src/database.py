import pyodbc

# MSSQL bağlantı fonksiyonu
def get_connection():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=BOZKURT;"          # bilgisayar adı
        "DATABASE=FactoryDB;"      # oluşturduğun veritabanı adı
        "Trusted_Connection=yes;"
    )
    return conn


# Sensör verisini veritabanına ekleme
def insert_sensor_data(sicaklik, basinc, uretim):

    conn = get_connection()     # veritabanına bağlan
    cursor = conn.cursor()      # SQL komut çalıştırma aracı

    query = """
    INSERT INTO SensorData (sicaklik, basinc, uretim)
    VALUES (?, ?, ?)
    """

    cursor.execute(query, (sicaklik, basinc, uretim))
    conn.commit()               # veriyi kaydet
    conn.close()                # bağlantıyı kapat


# API'nin kullanacağı veri çekme fonksiyonu
def get_last_data():

    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT TOP 10 * FROM SensorData ORDER BY id DESC"
    cursor.execute(query)

    rows = cursor.fetchall()    # tüm satırları al
    conn.close()

    return rows