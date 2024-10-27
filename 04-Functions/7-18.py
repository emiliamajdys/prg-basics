def f(number):
    
    str_number = str(number)
    digit_count = {}
    
    
    for digit in str_number:
        if digit in digit_count:
            digit_count[digit] += 1
        else:
            digit_count[digit] = 1

    
    repeated_sum = sum(int(digit) * count for digit, count in digit_count.items() if count > 1)

    return repeated_sum


number = int(input('Enter a number: '))
result = f(number)
print(result)
