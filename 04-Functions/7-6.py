def ifbinary(char):
    for char in number:  
        if char !="0" and char!= "1":
            return False
        else: 
            return True
        
number = input('Insert the number: ')
final = ifbinary(number)
print(final)
