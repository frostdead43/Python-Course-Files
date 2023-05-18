import random
sayi = random.randint(1,10)
can = int(input("can sayisi gir "))
hak = can
sayac = 0

while hak > 0:
    hak-=1
    sayac+=1
    tahmin = int(input("tahmininiz "))

    if sayi == tahmin:
        print(f"tebrikler {sayac}. hakkinda bildin. Toplam puanin : {100- (20)*(sayac-1)}")
        break
    elif sayi > tahmin:
        print("yukari")
    else:
        print("asagi")

    if hak == 0:
        print(f"tahmin bitti. Tutulan sayi : {sayi}")


