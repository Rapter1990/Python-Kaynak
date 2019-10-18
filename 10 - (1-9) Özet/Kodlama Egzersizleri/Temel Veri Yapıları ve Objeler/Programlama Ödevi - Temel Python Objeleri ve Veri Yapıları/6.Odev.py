print("Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.")

a = int(input("Birinci kenarı giriniz :"))
b = int(input("İkinci kenarı giriniz :"))

hipotenuz = (a ** 2) + (b ** 2)
hipotenuz = hipotenuz **0.5

print("Hipotenüz : {}".format(hipotenuz))