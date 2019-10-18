print("""
************************
Kullanıcı Girişi
************************
""")

sys_kullanici_adi ="Noyan"
sys_sifre = "123456"

kullanıcı_adi = input("Kullanıcı adı :")
sifre = input("Şifre :")

if(kullanıcı_adi == sys_kullanici_adi and sifre == sys_sifre):
    print("Sisteme hoşgeldiniz...")
elif( (kullanıcı_adi != sys_kullanici_adi and sifre == sys_sifre) or (kullanıcı_adi == sys_kullanici_adi and sifre != sys_sifre)):
    print("Kullancı adı veya şifre hatalı")
else:
    print("Kullancı adı ve şifre hatalı")