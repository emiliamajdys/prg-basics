def f(arr1,arr2):
    if arr1[0]==arr2[0] and arr1[1]==arr2[1] and arr1[2]==arr2[2]:
        return True
    else:
        return False
    
arr1=["water","book","sky"]
arr2=["water","book","sky"]
true=f(arr1,arr2)
print(true)