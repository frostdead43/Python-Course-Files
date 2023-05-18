MakoHesap = {
"isim" : "Mako Kyilmaz",
"hesapNo": "123456789",
"bakiye": 3000,
"ekHesap": 2000
}

AysunHesap = {
"isim" : "Aysun Kyilmaz", 
"hesapNo": "987654321",
"bakiye": 2000,
"ekHesap": 1000
}

def paracek(hesap,miktar):
    print(f'Merhaba {hesap["isim"]}')

    if(hesap['bakiye']>= miktar):
        hesap['bakiye']-= miktar
        print(" paranizi alabilirsiniz. ")
    else:
        toplam = hesap ["bakiye"] + hesap["ekHesap"]
        if (toplam>=miktar):
            ekHesapkullanilsinmi = input("ek hesap kullanilsin mi (e/h)")

            if ekHesapkullanilsinmi == 'e':
                bakiye = hesap ['bakiye']

                ekhsapkulmik = miktar - hesap['bakiye']

                hesap['bakiye']= 0
                hesap['ekHesap']-= ekhsapkulmik


                print("paranizi alabilirsiniz")
            else:
                print(f'{hesap["hesapNo"]} nolu hesabinizda {hesap["bakiye"]} bulunmaktadir.')    
        else:
            print("üzgünüz, bakiyeniz yetersiz!")        

paracek(MakoHesap,5000)
paracek(MakoHesap,2000)