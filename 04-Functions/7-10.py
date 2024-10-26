def f(n1,n2,n3):
    if n1<0 or n2<0 or n3<0:
       return True
    else:
       return False

num1=int(input('insert the n1: '))
num2=int(input('insert the n2: '))
num3=int(input('insert the n3: '))
answ=f(num1,num2,num3)
print(answ)