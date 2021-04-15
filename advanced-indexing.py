digits = [0,1,2,3,4,5,6,7,8,9]
# name = "first last"

# print(digits[0])

# print(digits[-3])

# print(digits[-len(digits)])

# #slicing
# print(digits[:3])
# print(name[:5])

# print(digits[0:-1])
# print(digits[5:])

# #striding
# print(digits[::-2])
# print(digits[0:10:3])
# print(digits[5:0:-2])

# #len = length
# for i in range(len(digits)):
#     print(digits[0:i])

# for i in range(len(digits)):
#     print(digits[0:i:3])

# for i in range(len(digits)):
#     print(digits[i:i+3])

window_size = 3
less_iterations = window_size - 1

#the - less_iterations means that it will set a limit to the number of iterations returned
for i in range(len(digits) + less_iterations):
    print(digits[i:i+window_size])