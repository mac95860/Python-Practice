#allows you to make lists from expressions

names = ["Mike", "Gabby", "John", "Mark"]

l = []

for person in names:
    l.append(person)

print(l)

print([person for person in names])

l = []
for person in names:
    l.append(person + ' ran away')
print(l)

print([person + ' ran away' for person in names])

movies_and_ratins = {"INterstellar": 9, "Dark Knight": 8, "House Party": 5, "Star Wars": 7} 

l = []
for movie in movies_and_ratins:
    if movies_and_ratins[movie] > 6:
        l.append(movie)

print(l)

print( [movie for movie in movies_and_ratins if movies_and_ratins[movie] > 6] )