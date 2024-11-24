import random 
def rand_elem(array):
    return random.choice(array)


array=[10,20,30,40,50,60]
final1=rand_elem(array)
final2=rand_elem(array)
final3=rand_elem(array)
print(final1,final2,final3)