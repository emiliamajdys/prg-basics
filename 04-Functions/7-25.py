def f(text):
    n = ''
    for char in text:  
        n += char + ' '  
    return n.strip()  

word = str(input('Insert the word: '))
final = f(word)
print(final)
