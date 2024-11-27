translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}
translate=input('the word i want to translate is: ')

def f(translate):
    if translate in translations:

        print(translations[translate])
    else:
        print(False)

f(translate)