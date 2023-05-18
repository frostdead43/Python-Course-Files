#1-Workbench IDE ile schooldb isminde bir database olusturup Student tablosunu ekleyiniz.
#Id,StudentNumber,Name,Surname,Birthdate,Gender


#2-Database baglantısını oluştur

#3- Aşağıdaki bilgiler için insert sorguları oluşturup kayıtları ekleyiniz.

#("101","Ahmet","Yılmaz",datetime.datetime(2005,5,17),"E")
#("102","Ali","Can",datetime.datetime(2005,6,17),"E")
#("103","Canan","Tan",datetime.datetime(2005,7,7),"K")
#("104","Ayşe","Taner",datetime.datetime(2005,9,23),"K")
#("105","Bahadır","Toksöz",datetime.datetime(2004,4,27),"E")
#("106","Ali","Cenk",datetime.datetime(2003,8,25),"E")

import mysql.connector
import datetime
from connectionsql import connection

class Student:
    connection = connection
    mycursor = connection.cursor()


class Student:
    def __init__(self,studentNumber,name,surname,birthdate,gender):
        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender

    def saveStudent(self):
        sql = "INSERT INTO Student(StudentNumber,Name,Surname,Birthdate,Gender) VALUES (%s,%s,%s,%s,%s)"
        values = (self.studentNumber,self.name,self.surname,self.birthdate,self.gender)
        Student.mycursor.execute(sql,values)
    try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayit eklendi")
    except mysql.connector.Error as err:
            print("hata",err)
    finally:
            Student.connection.close()



ahmet = Student("202","Ahmet","Yilmaz",datetime.datetime(2006,5,6),"E")
ahmet.saveStudent()
mehmet = Student("206","Mako","kyilmaz",datetime.datetime(2007,5,1),"E")
mehmet.saveStudent()



# ögrenciler = [
#     ("101","Ahmet","Yilmaz",datetime.datetime(2005,5,17),"E"),
#     ("102","Ali","Can",datetime.datetime(2005,6,17),"E"),
#     ("103","Canan","Tan",datetime.datetime(2005,7,7),"K"),
#     ("104","Ayşe","Taner",datetime.datetime(2005,9,23),"K"),
#     ("105","Bahadir","Toksöz",datetime.datetime(2004,4,27),"E"),
#     ("106","Ali","Cenk",datetime.datetime(2003,8,25),"E")
# ]

# mycursor.executemany(sql,ögrenciler)

# try:
#     connection.commit()
#     print(f"{mycursor.rowcount} tane kayit eklendi")
# except mysql.connector.Error as err:
#     print("hata",err)
# finally:
#     connection.close()