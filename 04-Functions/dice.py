def f(dice):
    maxi=0
    count=0
    for i in range(1,len(dice)):
     if dice[i]==dice[i-1]:
        count+=i
     else:
        maxi=max(maxi,count)
    maxi=max(maxi,count)
    return maxi
dice=str(input('dice: '))
print(f(dice))