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


def tum_verileri_getir():
    cursor.execute("SELECT * FROM kitaplık")
    liste = cursor.fetchall()
    print("Kitap Listesi\n*************************************")
    for i in liste:
        print("İsim : {}\nYazar : {}\nYayınevi : {}\nSayfa Sayısı:{}\n*******************".format(i[0],i[1],i[2],i[3]))


def isim_yazar_verileri_getir():
    cursor.execute("SELECT isim,yazar FROM kitaplık")
    liste = cursor.fetchall()
    print("Kitap Tablosunu Bilgileri\n*************************************")
    for i in liste:
        print(i)

def yayınevi_getir(yayınevi):
    cursor.execute("SELECT * FROM kitaplık WHERE Yayınevi = ?",(yayınevi,)) # değişken bir tane olduğundan demet(tuple) , dedik
    liste = cursor.fetchall()
    print("Kitap Listesi\n*************************************")
    for i in liste:
        print("İsim : {}\nYazar : {}\nYayınevi : {}\nSayfa Sayısı:{}\n*******************".format(i[0],i[1],i[2],i[3]))


def yayınevi_veriyi_güncelle(eski_yayınevi,yeni_yayınevi):
    cursor.execute("UPDATE kitaplık SET Yayınevi = ? WHERE Yayınevi = ?",(yeni_yayınevi,eski_yayınevi))
    con.commit()

def yazar_sil(yazar):
    cursor.execute("DELETE FROM kitaplık WHERE Yazar = ?",(yazar,))
    con.commit()

# VERİ GÜNCELLELEME
#tum_verileri_getir()
#eski_yayınevi = input("Yayınevi adını giriniz :")
#yeni_yayınevi = input("Yeni Yayınevi adını giriniz :")
#yayınevi_veriyi_güncelle(eski_yayınevi,yeni_yayınevi)
#tum_verileri_getir()

# VERİ SİLME
tum_verileri_getir()
yazar = input("Silmek istediğiniz kitabın yazarını giriniz :")
yazar_sil(yazar)
tum_verileri_getir()


con.close() # Veritabanı bağlantısını kapatma




