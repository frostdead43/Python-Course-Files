#class
class Person:
    #class attributes
    address = "no information"
    #constructor (yapıcı metod)
    def __init__(self,name,year):
        #object attributes
        self.name = name
        self.year = year
        print("init metodu çalişti.")

        #methods (instance)
        def intro(self):
            print("hello there")


#object(instance)
p1 = Person ("Mako",1996)
p2 = Person ("Aysun",1974)

#######
# print(f"p1: name: {p1.name}, year: {p1.year}")
# print(f"p2: name: {p2.name}, year: {p2.year}")
#######


print(p1)
print(p2)
print(type(p1))
print(type(p2))