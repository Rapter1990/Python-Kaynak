import sqlite3 # Sqlite'yı dahil ediyoruz

con = sqlite3.connect("kütüphane.db") # Tabloya bağlanıyoruz

cursor = con.cursor() # cursor isimli değişken veritabanı üzerinde işlem yapmak için kullanacağımız imleç

def tablo_olustur():
    cursor.execute("""CREATE TABLE IF NOT EXISTS kitaplık (isim TEXT,
                   Yazar TEXT,Yayınevi TEXT,Sayfa_Sayisi INT)""")
    con.commit() # yukarıdaki kodun çalışması ve kütüphan.db eklenmesi için bu kodu yazdık


def veri_ekle():
    cursor.execute("""INSERT INTO kitaplık VALUES ('İstanbul Hatırası',
'Ahmet Ümit','Everest',561)
""")
    con.commit()

def veri_ekle2(isim,yazar,yayınevi,sayfa_sayısı):
    cursor.execute("INSERT INTO kitaplık VALUES (?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayısı))
    con.commit()

isim = input("İsim :")
yazar = input("Yazar :")
yayınevi = input("Yayın Evi :")
sayfa_sayısı = int(input("Sayfa Sayısı :"))

veri_ekle2(isim,yazar,yayınevi,sayfa_sayısı)

con.close() # Veritabanı bağlantısını kapatma




