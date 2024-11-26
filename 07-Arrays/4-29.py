def create_2d_arr(x,y):
    return [[0 for _ in range(x)] for _ in range(y)] 

function=create_2d_arr(3,5)
for row in function:
    print(row)