print("""

Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.

Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi , dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.

Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı , eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın. Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.o

Üçgen belirtme şartını bilmiyorsunuz internetten bakabilirsiniz.

Ayrıca , bu problemde mutlak değer bulmaya ihtiyacınız olacak. Bunun için, Pythonda hazır bir fonksiyon olan abs() fonksiyonunu kullanabilirsiniz. Kullanımı şu şekildedir ;

""")

tip = input("Hesaplamak istediğiniz geometrik şekli giriniz ( Üçgen / Dörtgen ) :")

if tip == "Dörtgen":
    print("***************************"
          "Dörtgen İşlemi"
          "***************************")
    print("----------Dörtgen Kenarlarını Giriniz----------- ")
    a = int(input("1.Kenar : "))
    b = int(input("2.Kenar : "))
    c = int(input("3.Kenar : "))
    d = int(input("4.Kenar : "))

    if a == b == c == d :
        print("KARE...")
    elif  a == b and (a != c and b != c) and (a != d and b != d) and c == d :
        print("DİKDÖRTGEN...")
    elif b == c and (b != a and c != a) and (b != d and c != d) and a == d :
        print("DİKDÖRTGEN...")
    elif a == c and (a != b and c != b) and (a != d and c != d) and b == d :
        print("DİKDÖRTGEN...")
    else:
        print("DÖRTGEN...")


elif tip == "Üçgen":
    print("***************************"
          "Üçgen İşlemi"
          "***************************")
    print("----------Üçgen Kenarlarını Giriniz----------- ")
    a = int(input("1.Kenar : "))
    b = int(input("2.Kenar : "))
    c = int(input("3.Kenar : "))

    if a == b == c:
        print("EŞKENAR...")
    elif a==b and (a !=c and b !=c):
        print("İKİZKENAR...")
    elif a==c and (a !=b and c !=b):
        print("İKİZKENAR...")
    elif b==c and (b != a and c != a):
        print("İKİZKENAR...")
    elif (abs(b-c) < a < b + c) and (abs(a-c) < b < a + c) and (abs(a-b) < c < a + b):
        print("ÜÇGEN...")
    else:
        print("ÜÇGEN BELİRTMİYOR...")
else:
    print("Hata")