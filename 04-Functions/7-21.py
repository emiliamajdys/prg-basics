def f(name):
    
    acronym = ''.join(word[0].upper() for word in name.split())
    return acronym


input_text = input('Enter a text: ')
result = f(input_text)
print(result)
