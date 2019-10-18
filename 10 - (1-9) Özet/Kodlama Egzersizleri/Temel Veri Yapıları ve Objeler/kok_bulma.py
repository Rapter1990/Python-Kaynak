"""

 2. dereceden bir bilinmeyenli denkelemin köklerini bulma

 Denklem = ax^2 + bx + c

 Delta hesaplama = b **2 -4 * a *c

 Birinci Kök : (-b - delta ** 0.5 ) / 2 *a
 İkinci Kök : (-b + delta ** 0.5 ) / 2 *a

"""

print("2. dereceden bir bilinmeyenli denkelemin köklerini bulma")

a = int(input("a :"))
b = int(input("b :"))
c = int(input("c :"))

delta = b **2 -4 * a *c

x1 = (-b - (delta ** 0.5) ) / (2 *a)
x2 = (-b + (delta ** 0.5) ) / (2 *a)

print("Birinci Kök : {}\n"
      "İkinci Kök : {}".format(x1,x2))