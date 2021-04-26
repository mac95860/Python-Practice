from collections import OrderedDict

dictionary = {
    'bananas': 3,
    'oranges': 4
}

# dictionaries are a way to organize data into key:value pairs
print(dictionary['bananas'])
print(dictionary.get('oranges'))
# returns none
print(dictionary.get('Hello'))

contacts = {
    'Joe': {
        'phone': '123-4567', 
        'email': 'joe@email.com'
        },
    'Jane': [
        '987-6543', 
        'jane@email.com'
        ]
}

print(contacts['Joe'])
print(contacts['Joe']['phone'])

sentence = "I like the name Mike because the name Mike is the best"

word_count = {

}

#dict.items
#dict.keys
#dict.vvalues

print(dictionary.items())
print(dictionary.keys())
#dict.pop
#dict.popitem, removes arbitrary last item. pops out key and value as tuple
#dict.clear()
#sort(dict)
