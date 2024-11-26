arr=[
    [1,2,3,5,4],
    [2,3,4,6,7],
    [9,8,0,1,2]

]
for row in arr:
    print(row)

arr[0],arr[-1]=arr[-1],arr[0]

for row in arr:
    print(row)