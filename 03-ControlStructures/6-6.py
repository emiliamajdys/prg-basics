time = int(input('insert the hours of parking '))

if 2>=time>=1:
    print('the price is 5PLN')
elif 6>=time>=3:
    print('the price is 15PLN')
elif time>6:
    print('the price is 20PLN')