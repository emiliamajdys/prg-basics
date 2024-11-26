array=[
        [-38, 19],
        [5,40],
        [-7,11],
        [29,16]
        ]
maximum = max(max(row) for row in array) 
minimum = min(min(row) for row in array) 

for i in range(len(array)):
    for j in range(len(array[i])):
        if array[i][j]==maximum:
            print(f'the maximum is in {i+1} and {j+1}' )
        if array[i][j]==minimum:
            print(f'the minimum is in {i+1} and {j+1}' )