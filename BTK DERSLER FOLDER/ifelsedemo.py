# soru 1 ****
# isim = input("isim giriniz :")
# yas = int(input("yas giriniz: "))
# egitim = input("egitim durumu: ")

# if (yas >= 18):
#     if(egitim=="lise" or egitim=="üniversite"):
#         print(f"{isim} ehliyet alabilirsin!")
#     else:
#         print(f"{isim} ehliyet alaman, egitim durumun yetersiz!")
# else:
#     print(f"{isim} ehliyet alaman, yasin tutmuyor!")       
         


# soru 2 ****
# yazili1 = float(input("yazili 1: "))
# yazili2 = float(input("yazili 2: "))
# sözlü = float(input("sözlü: "))

# ortalama = (yazili1+ yazili2+sözlü)/3

# if (ortalama>=0) and (ortalama<25):
#     print(f"ortalamaniz: {ortalama} notunuz: 0")
# elif(ortalama>=25) and (ortalama<45):
#     print(f"ortalamaniz: {ortalama} notunuz: 1")   
# elif (ortalama>=45) and (ortalama<55):
#     print(f"ortalamaniz: {ortalama} notunuz: 2")
# elif (ortalama>=55) and (ortalama<69):
#     print(f"ortalamaniz: {ortalama} notunuz: 3")
# elif (ortalama>=70) and (ortalama<85):
#     print(f"ortalamaniz: {ortalama} notunuz: 4")
# elif (ortalama>=85) and (ortalama<100):
#     print(f"ortalamaniz: {ortalama} notunuz: 5")
# else:
#     print("yanlis bilgi girdiniz!")   

import datetime


tarih = (input("araciniz hangi tarihte trafige cikti? (2020/1/9): "))
tarih = tarih.split('/')

trafigecikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi = datetime.datetime.now()
fark = simdi-trafigecikis
days=fark.days



if (days<=365):
    print("1.bakim yili ")
elif days > 365 and days <=365*2:
    print("2.bakim yili ")   
elif days > 365*2 and days <=365*3:
    print("3.bakim yili ")
else:
    print("hatali kullanim")

      