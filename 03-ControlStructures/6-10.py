humanage= int(input('enter the age of the dog in human years: '))

if humanage<=2:
    age=10.5*2
    print(f'the age in dog years is {age}')
else:
    age= 21+ (humanage-2)*4
    print(f'the age of the dog in dog years is {age}')
