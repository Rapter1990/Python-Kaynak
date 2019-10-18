print("Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.")

a = int(input("Birinci Sayı :"))
b = int(input("İkinci Sayı :"))

print()
print("Birinci Sayı : {}\n"
      "İkinci Sayı : {}".format(a,b))
print()

print("Yer Değiştirme")

a,b = b,a
print("Birinci Sayı : {}\n"
      "İkinci Sayı : {}".format(a,b))