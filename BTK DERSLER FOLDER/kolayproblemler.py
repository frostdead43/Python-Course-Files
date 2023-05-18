#ekrandan alinan bir sayinin faktoriyelini hesaplayan bir program yazınız.***

# sayi = int(input("sayi gir: "))

# faktoriyel = 1 

# i = 2

# while i <= sayi:
#     faktoriyel *= i
#     i += 1

# print(f"{sayi}!= {faktoriyel}")


#ekrandan alınan bir sayinin asal olup olmadığını kontrol eden bir program yazınız.***

# sayi = int(input("sayi gir: "))

# asal = True

# for i in range(2,sayi):
#     if sayi %i == 0:
#         asal = False
#         break
# if asal == True:
#     print(f"{sayi} sayisi asaldir!")
# else:
#     print(f"{sayi} sayisi asal degildir!")


#ekrandan alınan bir  sayinin pozitif kaç tane böleni old. bulan bir program yazınız.***

# sayi = int(input("sayi gir: "))

# bolen_sayisi = 0

# for i in range (1,sayi+1):
#     if sayi % i == 0:
#         bolen_sayisi += 1

# print(f"{sayi} sayisinin {bolen_sayisi} tane böleni vardir.")


#ekrandan okunan bir sayının rakamları toplamını hesaplayan bir program yazınız.***

# sayi = int(input("sayi gir: "))

# str_sayi = str(sayi)
# toplam = 0
# for rakam in str_sayi:
#     toplam += int(rakam)
# print(toplam)    


#ekrandan peşpeşe okunan 5 sayının  en küçüğünü ve en büyüğünü ekrana yazdıran bir program yazınız.***

# liste = []
# for i in range(5):
#     sayi = int(input("sayi gir: "))
#     liste.append(sayi)

# print(f"en büyük sayi: {max(liste)}")
# print(f"en küçük sayi: {min(liste)}")


#ekrandan okunan bir sayının herhangi bir sayının karesi olup olmadığını kontrol eden bir program yazınız.***

# sayi = int(input("sayi gir: "))

# karekök = sayi ** 0.5
# if karekök == int(karekök):
#     print("tamkare")
# else:
#     print("tamkare değil")   


#ekrandan okunan bir metinde hangi harfin kaç kere kullanıldığını gösteren bir program yazınız.***

# metin = input("metin gir: ")

# sözlük = dict()

# for harf in metin:
#     if harf in sözlük:
#         sözlük[harf] +=1
#     else:
#         sözlük[harf] = 1

# for harf,adet in sözlük.items():
#     print(harf,adet)


#ekrandan okunan bir metinde a harflerini büyük yapan bir program yazınız.***

metin = input("metin gir: ")
metin2 = ""

for harf in metin:
    if harf == "a":
        metin2 += "A"
    else:
        metin2 += harf
print(metin2)
