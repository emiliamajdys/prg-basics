def f(dice):
    max_streak = 0  
    current_streak = 1  

    for i in range(1, len(dice)):
        if dice[i] == dice[i - 1]:  
            current_streak += 1  
        else:
            max_streak = max(max_streak, current_streak) 
            current_streak = 1  

    
    max_streak = max(max_streak, current_streak)

    return max_streak


dice_sequence = input('Enter the sequence of dice rolls: ')
result = f(dice_sequence)
print(result)
