import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

def brackets_ok(expression):
 if brackets_ok(expression):
   return True

if brackets_ok(expression1):
   print(True)
else:
   print(False)

if brackets_ok(expression2):
    print(False)
else:
    print(True)