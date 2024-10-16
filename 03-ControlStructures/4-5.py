###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
     char=ord(char)
     char= char + 1
     char=chr(char)
     encrypted_text+=char

print(plain_text )
print(encrypted_text)
