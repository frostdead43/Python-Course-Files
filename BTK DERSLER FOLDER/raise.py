# x = 10

# if x > 5:
#     raise Exception("x 5 den büyük değer alamaz!")


import re


def check_password(psw):
    if len(psw) < 8:
        raise Exception("parola en az 7 karakter olmalidir.")
    elif not re.search("[a-z]",psw):
        raise Exception("parola kücük harf icermelidir")  
    elif not re.search("[A-Z]",psw):
        raise Exception("parola büyük harf icermelidir") 
    elif not re.search("[0-9]",psw):
        raise Exception("parola rakam icermelidir")    
    elif  re.search("\s",psw):
        raise Exception("parola bosluk icermemelidir")      
    else:
        print("Gecerli parola!")    
password = "12345678aA"

try:
    check_password(password)
except Exception as ex:
    print(ex)
else:
    print("gecerli parola!")    
finally:
    print("validation tamamlandi")    