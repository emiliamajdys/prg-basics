def is_prime(number):
    for i in range(2, int(number**0.5) + 1):
        if number%i==0:
            return False
        else:
            return True
        
def f(n):
    
    if n < 1:
        return None 

    count = 0  
    number = 1  

    while count < n:
        number += 1  
        if is_prime(number):
            count += 1  

    return number  


n = int(input('Enter the value of n: '))
result = f(n)
print(result)
        

