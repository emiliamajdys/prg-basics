def f(palindrome):
    
    normalized = ''.join(palindrome.split()).lower()
    
    return normalized == normalized[::-1]

n=str(input('give a word: '))
final=f(n)
print(final)

