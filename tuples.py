#tuple is a list with constraints ()

# you cannot add or remove elements from tuples, however they can be overwritten

t = (1,2,3)

credit_card1 = (1111222233334444, "Joe Rogan", "12/20", 123)
credit_card2 = (1111222233334444, "Tyron Biggins", "12/20", 123)

credit_cards = [credit_card1, credit_card2]

print(credit_cards)


person1 = ('Nancy', 25, 'Pizza')
person2 = ('Joe', 30, 'Burgers')

people = [person1, person2]


#think of this as object deconstruction, () are optional.This is called "Unpacking" in python
# name, age, favfood = person

# print(name)
# print(age)
# print(favfood)

for name, age, favfood in people:
    print(name)
    print(age)
    print(favfood)
    print('')
