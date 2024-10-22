###
# Program for testing built-in functions
#
max_number = max(7,5,6,3,8,2)
print('Max number of 7,5,6,3,8,2 is', max_number)

min_number = min(4,7,2,3,9,8)
print('Min number of 4,7,2,3,9,8 is', min_number)

str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)

letter = (input('insert the letter: '))
print(f'the letter is {letter}')

number = 20303
new_number= chr(number)
print(f'the number converted into string is {new_number}')

numbers=bin(304)[2::]
print(numbers)

numberh=hex(304)[2::]
print(numberh)

print(f'€ {ord('€')}')

import math
numbera= abs(-17)
print(numbera)