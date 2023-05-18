import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "75116424563",
    database = "mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("Create Table customers (name VARCHAR(255), adress VARCHAR(255))")

# mycursor.execute("Create Database mydatabase")
# mycursor.execute("Show Databases")

# for i in mycursor:
#     print(i)
