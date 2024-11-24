def bubblesort(array):
    n = len(array)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                
    return array

arr1=[2,4,5,1,2,7]
true=bubblesort(arr1)
print(true)