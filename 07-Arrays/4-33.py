array=[
    [1,2,3,4,5],
    [6,7,8,9,0],
    [11,12,13,14,15]
]

for row in array:
    print(row)

array[0][0], array[0][-1]= array[0][-1], array[0][0]
array[1][0], array[1][-1]= array[1][-1], array[1][0]
array[2][0], array[2][-1]= array[2][-1], array[2][0]
for row in array:
    print(row)