import re

text=input('the text is: ')
pattern='[AaEeOoUuIi]'

vowels=re.findall(pattern,text)

print(len(vowels))
