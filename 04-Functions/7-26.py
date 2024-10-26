def f(product):
    if len(product)!=4:
        print('this is not 4 digit')

    if (int(product[0]) + int(product[1]) + int(product[2]))%(int(product[3])) == 0:
        return True
    else: 
        return False
    
code=str(input('give the 4 digit code: '))
final=f(code)
print(final)