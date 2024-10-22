###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides

def triangle_area(a,b,c):
    obwpol = (a + b + c)/2
    area = obwpol(obwpol-a)(obwpol-b)(obwpol-c)**0,5

    return area

a=input('insert the a: ')
b=input('insert the b: ')
c=input('input the c: ')

triangle=triangle_area


print(f'The area of ​​a triangle with sides {a,b,c} is {triangle}')

