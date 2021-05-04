list1 = [1,2,3,4,5]
list2 = ['one', 'two', 'three', 'four', 'five']

#must use this syntax in Python 3

#python will always trunkate and conform to the shortest list length
zipped = list(zip(list1, list2))
print(zipped)

# returns
# [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')]

unzipped = list(zip(*zipped))
print(unzipped)

# returns
# [(1, 2, 3, 4, 5), ('one', 'two', 'three', 'four', 'five')]

# for (l1 , l2) in zip(list1, list2):
#     print(l1)
#     print(l2)

items= ['Apple', 'Banana', 'Orange']
counts = [3,2,5]
prices = [0.99, 0.25, 0.50]

sentences = []

for (item, count, price) in zip(items, counts, prices):
    item, count, price = str(item), str(count), str(price)
    sentence = "I bought " + count + ' ' + item + 's at ' + price + '.'
    sentences.append(sentence)

# by not indenting the print statement, the statement has been moved outside of the for loop
print(sentences)  

# returns
# [
#     'I bought 3 Apples at 0.99.', 
#     'I bought 2 Bananas at 0.25.', 
#     'I bought 5 Oranges at 0.5.'
#     ]

for sentence in sentences:
    print(sentence)
