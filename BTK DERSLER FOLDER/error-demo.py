liste = ["1","2","5a","10b","abc","10","50"]

#Soru1****

# for x in liste:
#     try:
#         result = int(x)
#         print(result)
#     except ValueError:
#         continue    


#Soru2****

# while True:
#     sayi = input("sayi: ")
#     if sayi == "q":
#         break
    
#     try:
#         result = float(sayi)
#         print("girdiginiz sayi: ", result)
#     except ValueError:
#         print("gecersiz sayi")
#         continue    


#Soru3****

# turkceKarakterler = 'şçğüöıİ'

# parola = input("parola: ")

# for i in parola:
#     if i in turkceKarakterler:
#         raise TypeError("parola türkce karakter iceremez!")
#     else:
#         pass    
# print("gecerli parola")


#Soru4****

def faktoriyel(x):
    x = int(x)

    if x < 0:
        raise ValueError("Negatif deger")


    result = 1

    for i in range(1, x+1):
        result *= i

    return result    

for x in [5,10,20,-3,"10a"]:
    try:
        y = faktoriyel(x)
    except ValueError as err:
        print(err)
        continue

    print(y)        
