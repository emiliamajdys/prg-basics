arr= [
   [0,0,0],
   [0,0,0],
   [0,0,0]
]

arr[0][0]=1
arr[1][1]=1
arr[2][2]=1
for row in arr:
    for item in row:
        print(item, end=" ")
    print()