#error handling
try:
    x = int(input("x: "))
    y = int(input("y: "))
    print(x/y)
except ZeroDivisionError:
    print("y için 0 girilemez!")
except ValueError:
    print("yanlis bilgi verdiniz")
else:
    print("hersey yolunda") #break de yazabilirsin döngüyü tekrar ettirir.
finally:
    print("try except sonlandi")    



    
