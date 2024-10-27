def f(n1,n2,n3):
    if n1>n2>n3:
        sum=n1-n3
    elif n2>n3>n1:
        sum=n2-n1
    elif n1>n3>n2:
        sum=n1-n2
    elif n2>n1>n3:
        sum=n2-n3
    elif n3>n1>n2:
        sum=n3-n2
    elif n3>n2>n1:
        sum=n3-n1
    else:
         return False
    
    return sum


n1=int(input("inserrt the n1: "))
n2=int(input("inserrt the n2: "))
n3=int(input("inserrt the n3: "))
final=f(n1,n2,n3)
print(final)