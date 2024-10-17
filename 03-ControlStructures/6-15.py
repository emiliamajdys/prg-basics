ean = input('insert the ean code: ')

if len(ean) == 13:
    print('the ean code is correct')

    if ean[0:3] == "590":
       
     print('Article manufactured in Poland')

else: 
   print('the code is not 13digit long')
       