def f(number,even):
    conut=0
    if even=="t":
        conut += number%2==0
    elif even=="f":
        conut += number%2!=0
    return conut

number=int(input('insert the numebrs: '))
even=str(input('(t/f): '))
final=f(number,even)
print(final)