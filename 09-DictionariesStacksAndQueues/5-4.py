winter_semester = {
   "math":60,
   "programming":30,
   "history":15
}

count=0 
for value in winter_semester.values():
    count+=value
   
print(f'The total number of hours in the winter semester is {count}')

