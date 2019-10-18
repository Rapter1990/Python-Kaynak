import sqlite3 # Sqlite'yı dahil ediyoruz

con = sqlite3.connect("kütüphane.db") # Tabloya bağlanıyoruz

cursor = con.cursor() # cursor isimli değişken veritabanı üzerinde işlem yapmak için kullanacağımız imleç

def tablo_olustur():
    cursor.execute("""CREATE TABLE IF NOT EXISTS kitaplık (isim TEXT,
                   Yazar TEXT,Yayınevi TEXT,Sayfa_Sayisi INT)""")
    con.commit() # yukarıdaki kodun çalışması ve kütüphan.db eklenmesi için bu kodu yazdık

tablo_olustur()

con.close() # Veritabanı bağlantısını kapatma




