# sets use {}
# sets cannot have duplicates i.e. {1,2,3,3} is not possible
s = {'banana', 'orange', 'blueberry', 'rasberry'}
# returns set in random order
print(s)

s.add('strawberry')
print(s)

s.add(4)
print(s)

s.add('blueberry')
print(s)
# that the set will only be randomized once each time the program is run regardless of number of calls when you try to add
# a duplicate. It does not return an error
s.add('blueberry')
print(s)

l = [1,2,3,3,4,4,4,5]
print(l)

# removes all duplicates and changes type from list to set
no_duplicate_set = set(l)
print(no_duplicate_set)

#changes the type back to list and returns list with no duplicates
no_duplicate_list = list(no_duplicate_set)
print(no_duplicate_list)

l = no_duplicate_list
print(l)

library_1 = {"Harry Potter", "LOTR", "Hunger Games"}
library_2 = {"Harry Potter", "Hamlet"}

# must new data set to a new variable
town = library_1.union(library_2)
print(town)

diff = library_1.difference(library_2)
print(diff)

at_both_libraries = library_1.intersection(library_2)
print(at_both_libraries)

library_1.clear()
# returns set()
print(library_1)