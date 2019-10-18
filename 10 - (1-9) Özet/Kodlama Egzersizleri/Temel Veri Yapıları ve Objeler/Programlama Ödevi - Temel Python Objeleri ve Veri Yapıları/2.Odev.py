print("Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.")

boy = int(input("Boyunuzu Giriniz : "))
kilo = int(input("Kilonunzu Giriniz :"))

beden_kitle_endeksi = kilo / (boy ** 2)

print("Beden kitle endeksi : {}".format(beden_kitle_endeksi))