x= int(input('insert the "x" data: '))
y= int(input('insert the "y" data: '))

if x>0 and y>0:
    print(f'your point {x,y} are in the 1  quadrant')
elif x>0 and y<0:
    print(f'your point {x,y} are in the 4  quadrant')
elif x<0 and y>0:
    print(f'your point {x,y} are in the 2  quadrant')
elif x<0 and y<0:
    print(f'your point {x,y} are in the 3  quadrant')
else:
    print('error')