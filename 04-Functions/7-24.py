x=input('insert the x: ')
y=input('insert the y: ')

def f(x, y):
    total_sum = 0
    for num in range(x, y + 1):
        if num % 6 == 0 and num % 4 != 0:
            total_sum += num
    return total_sum


