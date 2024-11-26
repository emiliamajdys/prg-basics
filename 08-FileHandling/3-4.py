###
# Calculates the total value of money spent
#
import re # module for regular expressions
import os
print(os.getcwd())


# file name with shopping report
email_file = 'raport.txt'

# read the content of email
with open(email_file, 'r') as file:
    email =file.read()

# regular expression pattern
# for amounts
pattern = '\d+'

# extract numbers from email
# tip: findall() method returns an array
amounts = re.findall(pattern, email)

# calculate the total purchases
count=0
for amount in amounts:
   count+=int(amount)

# print result
print(count)