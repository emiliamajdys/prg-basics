def f(n):
    return' '.join(str(i) for i in range(1,n+1))

number=int(input('insert the number'))
final=f(number)
print(final)