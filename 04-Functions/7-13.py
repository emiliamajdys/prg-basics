def f(number1, number2, operator): 
    math = 0  
    
    if operator == "-":
        math = number1 - number2
    elif operator == "*":
        math = number1 * number2
    elif operator == "+":
        math = number1 + number2
    elif operator == "**":
        math = number1 ** number2
    elif operator == "%":
        math = number1 % number2
    else:
        return 'To nie jest poprawny operator' 

    return math


operator = str(input('Wprowadź operator: '))
num1 = int(input('Wprowadź liczbę 1: '))
num2 = int(input('Wprowadź liczbę 2: '))


final = f(num1, num2, operator)
print(final)
