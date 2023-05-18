myList = [1,2,3]
# myString = "my string"

# print(len(myList))
# print(len(myString))
# print(type(myList))
# print(type(myString))


class Movie():
    def __init__(self,title,director,duration):
        self.title = title
        self.director = director
        self.duration = duration
        print("movie objesi olusturuldu")

    def __str__(self):
        return f"{self.title} by {self.director}"
    

    


        
m = Movie("film adi", "filmin yönetmeni","filmin süresi")

print(str(myList))
print(str(m))