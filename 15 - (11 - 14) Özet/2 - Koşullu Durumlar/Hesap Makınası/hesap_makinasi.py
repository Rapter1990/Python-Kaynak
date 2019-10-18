print("""
****************************

Hesap Makinası

İşlemler;

1 ) Toplama İşlemi

2 ) Çıkarma İşlemi

3 ) Çarpma İşlemi

4 ) Bölme İşlemi

****************************
""")

a = int(input("Birinci Sayiyi Giriniz :"))
b = int(input("İkinci Sayiyi Giriniz :"))

islem = input("İşlemi Giriniz :")

if islem == "1":
    print("{} ile {} toplamı = {}".format(a,b,(a+b)))
elif islem == "2":
    print("{} ile {} çıkarma = {}".format(a, b, (a - b)))
elif islem == "3":
    print("{} ile {} çarpma = {}".format(a, b, (a * b)))
elif islem == "4":
    print("{} ile {} bölme = {}".format(a, b, (a / b)))
else:
    print("Hata")