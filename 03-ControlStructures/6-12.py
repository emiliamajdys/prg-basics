number = int(input('insert the number of bought products'))
price = int(input('insert the price of the products '))
if number>2:
    pricea= number * price * 0.75
    
else :
    pricea = number * price 

print(f'the price is {pricea}') 
print(f'the amount of thing is {number}') 
print(f'the price of the single product is {price}')

