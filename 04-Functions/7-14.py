def f(detector):
    count = 0
    max_count = 0  
    
    for event in detector:
        if event == '+':
            count += 1  # A person enters
        elif event == '-':
            count -= 1  # A person leaves
        
        if count > max_count:
            max_count = count
            
    return max_count >= 3


jsjs=str(input('.'))
final=f(jsjs)
print(final)