translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}
translate=input('the word i want to translate is: ')

for key in translations.items():
    if translate==key:
        print(key)
    else:
        print(False)