print("""

Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.

    Vize1 toplam notun %30'una etki edecek.

    Vize2 toplam notun %30'una etki edecek.

    Final toplam notun %40'ına etki edecek.


    Toplam Not >=  90 -----> AA

    Toplam Not >=  85 -----> BA

    Toplam Not >=  80 -----> BB

    Toplam Not >=  75 -----> CB

    Toplam Not >=  70 -----> CC

    Toplam Not >=  65 -----> DC

    Toplam Not >=  60 -----> DD

    Toplam Not >=  55 -----> FD

    Toplam Not <  55 -----> FF

""")

vize1 = float(input("Vize 1 notunu giriniz :"))
vize2 = float(input("Vize 2 notunu giriniz :"))
final = float(input("Final notunuzu giriniz :"))

notu = (vize1 * 0.3) + (vize2 * 0.3) + (final * 0.4)
print("Not : {}".format(notu))

if notu >= 90:
    print("AA")
elif notu >= 85:
    print("BA")
elif notu >= 80:
    print("BB")
elif notu >=75:
    print("CB")
elif notu >=70:
    print("CC")
elif notu >=65:
    print("DC")
elif notu >= 60:
    print("DD")
elif notu >= 55:
    print("EF")
else:
    print("FF")