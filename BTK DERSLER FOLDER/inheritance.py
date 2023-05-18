class Person():
    def __init__(self,fname,lname):
        self.firstName = fname
        self.lastName = lname
        print("person created")

class Student(Person):
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)
        print("student created")
        


p1 = Person("mako","kyilmaz")
s1 = Student("aysun","kyilmaz")

print(p1.firstName+ " "+ p1.lastName)
print(s1.firstName+ " "+ s1.lastName)