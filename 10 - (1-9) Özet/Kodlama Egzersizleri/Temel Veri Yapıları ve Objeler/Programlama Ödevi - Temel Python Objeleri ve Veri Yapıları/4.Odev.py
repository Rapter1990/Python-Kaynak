print("Kullanıcıdan ad,soyad ve numara bilgisini alarak bunları alt alta ekrana yazdırın.")

ad = input("Ad :")
soyad = input("Soyad :")
numara = input("TC Numarası :")

bilgiler =[ad,soyad,numara]

print("Adı : {}\n"
      "Soyad : {}\n"
      "TC Numarası :{}".format(bilgiler[0],bilgiler[1],bilgiler[2]))