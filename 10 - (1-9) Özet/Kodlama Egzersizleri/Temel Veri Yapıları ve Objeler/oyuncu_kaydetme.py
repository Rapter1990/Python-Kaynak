print("Oyuncu Kaydetme Programı")

ad = input("Oyuncunun Adı :")
soyad = input("Oyuncunun Soyadı :")
takım = input("Oyuncunun Takımı :")

bilgiler = [ad,soyad,takım]

print("Bilgiler Kaydediliyor...")

print("Oyuncunun Adı : {}\n"
      "Oyuncunun Soyadı : {}\n"
      "Oyuncunun Takımı : {}".format(bilgiler[0],bilgiler[1],bilgiler[2]))

print("Bilgiler Kaydedildi.")