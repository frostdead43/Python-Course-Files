#RANGE****


# for item in range (0,50,10):
#     print(item)

# print(list(range (0,50,10)))

#ENUMERATE****

# index = 0
# greet = "hello there"

# for letter in greet:
#     print(f"index: {index} letter {letter}")
#     index +=1

# greet = "hello there"
# for item in enumerate(greet):
#     print(item)

#ZİP****

list1= [1,2,3,4,5]
list2= ['a','b','c','d','e']
list3= [100,200,300,400,500]

print(list(zip(list1,list2,list3)))

for item in zip(list1,list2,list3):
    print(item)

for a,b,c in zip(list1,list2,list3):
    print(a,b)