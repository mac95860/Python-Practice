l = [1,2,3]

# Booleans must be capitalized
other_list = [1, "strings", True, 4.3, [1,2,3]]

print(other_list)
print(other_list[1])

names = ["Joe", "John", "James"]

names.append("Jack")
print(names)

names.insert(2 ,"Jerrod")
print(names)

names.remove("John")
print(names)

names.reverse()
print(names)

numbers = [1, 4, 2, 69, 48, 32]
for i in numbers:
    print(i)

numbers.sort()
print(numbers)

numbers.sort()
numbers.reverse()
print(numbers)

# what goes into a list must be iterable, meaning it can go through each one, one at a time
for number in numbers:
    print(number)