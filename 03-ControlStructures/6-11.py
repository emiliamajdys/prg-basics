###A computer program analyses the price of a product in an online store. If the product price decreases by at least 10%, the program prints a purchase recommendation:

#Buy the product!!
#Product price reduced by 17%

price= int(input('enter the price: '))
decrease= int(input('enter the decrease in %: '))

if decrease>=10:
    print("buy the product!")
    print(f"product price reduced by {decrease}%")
    decrease_new=(100-decrease)/100
    new=price*decrease_new
    print(f"the new price is {new}")
    print(f'the old price is {price}')