###
# Prints some array elements
#
arr = [2, 3, 7, 5, 4]
new=""
print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print('last value',(arr[len(arr)-1]))
print('last value but one value', arr[-2])
print('middle value', arr[int(len(arr)/2)])


for i in range(len(arr)):
    print(arr[i], end =" ")
