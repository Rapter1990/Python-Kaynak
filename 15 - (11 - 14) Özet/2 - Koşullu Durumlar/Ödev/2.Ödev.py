print("Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.")

a = int(input("1.Sayi : "))
b = int(input("2.Sayi : "))
c = int(input("3.Sayi : "))

en_büyük_sayi = None

if( a >b and a > c):
    en_büyük_sayi = a
    print("En büyük sayı : {} ".format(a))

elif(b > a and b > c):
    en_büyük_sayi = b
    print("En büyük sayı : {} ".format(b))

elif(c > a and c > b):
    en_büyük_sayi = c
    print("En büyük sayı : {} ".format(c))

elif a == b or (a > c and b > c):
    print("En büyük sayı : a : {} ve  b : {} ".format(a,b))

elif b == c or (b > a and c > a):
    print("En büyük sayı : b : {} ve c : {} ".format(b,c))

elif a == c or (a > b and c > b):
    print("En büyük sayı : a : {} ve c : {} ".format(b,c))

else:
    print("Hepsi birinine eşitir.")