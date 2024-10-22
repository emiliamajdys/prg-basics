###
# Function that returns the full name of a day of the week
# based on its number
#
def day_name(day_number):
    result = ''
    if day_number == 1:
        result = 'Monday'
    elif day_number == 2:
        result = 'Tuesday'
    elif day_number == 3:
        result = 'Wednesday'
    elif day_number == 4:
        result = 'Thursday'
    elif day_number == 5:
        result = 'Friday'
    elif day_number == 6:
        result = 'Saturday'
    elif day_number == 7:
        result = 'Sunday'
    else:
        print('the inserted number is bigger than 7 and is not correct')
    
    
    return result

day=int(input('insert the day: '))
print(f'the day is {day} and the name for it is {day_name(day)}')