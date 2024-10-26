def f(n):
    asterisks=["*"]*n
    return '/'.join(asterisks)

number=int(input('insert the number: '))
final=f(number)
print(final)