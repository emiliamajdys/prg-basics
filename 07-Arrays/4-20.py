def separate_even_odd(array):
    evens = [num for num in array if num % 2 == 0]  
    odds = [num for num in array if num % 2 != 0]  
    return evens + odds  

arr = [7, 9, 2, 4, 5, 6]

result = separate_even_odd(arr)

print(arr)
print(result)

