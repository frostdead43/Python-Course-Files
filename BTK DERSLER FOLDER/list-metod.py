numbers = [1,10,5,16,4,9,10]
letters = ['a','g','s','b','y','a','s']

val = min(numbers)
val = max(numbers)
val = min(letters)
val = max(letters)


numbers[4] = 40

numbers.append(31)
numbers.append(69)
numbers.insert(5,43)
numbers.insert(-1,7)

numbers.pop(2)
numbers.remove(31)

numbers.sort()
letters.sort()


print(numbers)
print(letters)