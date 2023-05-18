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


def getProducts():
    connection = mysql.connector.connect(host="localhost",user= "root",password = "75116424563", database ="nodeapp") 
    cursor = connection.cursor()

    # cursor.execute("select * from Products") # tüm products kolonları
    cursor.execute("select name,price from Products")

    # result = cursor.fetchall() #tüm kayıtlar
    result = cursor.fetchone()
    print(f"name: {result[0]} price:{result[1]}")
    # for product in result:
    #     print(f"name: {product[1]} price:{product[2]}")
    #     print(f"name: {product[0]} price:{product[1]}")

getProducts()