def f(n):
    if n <= 0:
        return 0  
    elif n == 1:
        return 1 

    a, b = 0, 1  
    for _ in range(2, n):
        a, b = b, a + b  

    return b  

number=int(input('insert the number'))
final=f(number)
print(final)