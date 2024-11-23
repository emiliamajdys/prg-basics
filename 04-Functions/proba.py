def f(text):
    letters=["a","e","i", "o", "u", "y"]
    char=[letter for letter in letters]
    return text.count(char)
text=str(input(''))
print(f(text))