import mysql.connector


def insertProduct(name,price,imageUrl,description):
    connection = mysql.connector.connect(host="localhost",user= "root",password = "75116424563", database ="nodeapp") 
    cursor = connection.cursor()

    sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values =(name,price,imageUrl,description)
    cursor.execute(sql,values)

    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayit eklendi")
        print(f"son eklenen kaydin id numarasi: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("hata:",err)
    finally:
        connection.close()
        print("database baglantisi kapandi.")

def insertProducts(list):
    connection = mysql.connector.connect(host="localhost",user= "root",password = "75116424563", database ="nodeapp") 
    cursor = connection.cursor()

    sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values = list
    cursor.executemany(sql,values)

    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayit eklendi")
        print(f"son eklenen kaydin id numarasi: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("hata:",err)
    finally:
        connection.close()
        print("database baglantisi kapandi.")

list= []
while True:
    name = input("ürün adi gir:")
    price = input("ürün fiyati gir:")
    imageUrl = input("ürün resim adi gir:")
    description = input("ürün bilgisi gir:")

    list.append((name, price,imageUrl,description))

    result = input("devam etmek istiyor musunuz? (e/h)")
    if result == 'h':
        print("kayitlariniz veritabanina aktariliyor... ")
        print(list)
        insertProducts(list)
        break

insertProduct(name,price,imageUrl,description)


