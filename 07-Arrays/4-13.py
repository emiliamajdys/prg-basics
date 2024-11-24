def f(number, array):
    if number in array:
        print(number,"is in the array")
    else:
        print(number, "is not in the array")
    

number= int(input('number is'))
array=[15, 38, 7, 23, 14]
print(f(number,array))