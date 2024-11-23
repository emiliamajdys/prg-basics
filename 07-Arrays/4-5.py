arr = [15, 8, 31, 47, 2, 19]
total_sum = 0
count = 0
for item in arr:
    total_sum += item  
    count += 1  

average = total_sum / count if count != 0 else 0

print("Average of all items:", average)
