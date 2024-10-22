pin='0805'

for i in range(3):
    guess=input("enter the guessed pin: ")
    if guess==pin:
        print('pin is correct')
        break
    else:
        print('the pin is wrong, try again')
        
print('Sorry, your payment card has been blocked.')
