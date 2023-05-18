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

    cursor.execute("select * from Products Order By name, Price ") #siralama
    

    result = cursor.fetchall() #tüm kayıtlar
    # result = cursor.fetchone()
    
    for product in result:
        print(f"id: {product[0]} name: {product[1]} price:{product[2]}")
  


def getProductById(id):
    connection = mysql.connector.connect(host="localhost",user= "root",password = "75116424563", database ="nodeapp") 
    cursor = connection.cursor()
    
    sql = "Select * From products Where id=%s"
    params = (id,)

    cursor.execute(sql,params)

    # result = cursor.fetchall() #tüm kayıtlar
    result = cursor.fetchone()

    print(f"id:{result[0]} name:{result[1]} price:{result[2]}")
    
    # # # # for product in result:
    # # # #     print(f"name: {product[1]} price:{product[2]}")

def getProductInfo():
    connection = mysql.connector.connect(host="localhost",user= "root",password = "75116424563", database ="nodeapp") 
    cursor = connection.cursor()
    
    # sql = "Select Count(*) From products " #toplam count sayisi
    # sql = "Select Avg(Price) From products " #ortalama price
    # sql = "Select Sum(Price) From products " #toplam fiyat
    # sql ="Select Min(Price) From products "  #minimum fiyat
    # sql ="Select Max(Price) From products "  #maximim fiyat
    sql ="Select Name From products Where Price = (Select Max(Price) from products) " 
    cursor.execute(sql)

    # result = cursor.fetchall() #tüm kayıtlar
    result = cursor.fetchone()

    print(f"result:{result[0]}")
    
    

getProductInfo()