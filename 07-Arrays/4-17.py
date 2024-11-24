

def f(my_tuple,number):
    count=0
    for item in my_tuple:
        if item == number:
            count+=1
    return count

number=int(input('whats the value'))
my_tuple = (50,20,40,50,30,50)
true=f(my_tuple, number)
print(true)