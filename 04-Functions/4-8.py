hours = int(input('insert the hour:  '))
minutes= int(input('insert the minutes: '))
time_format= str(input('choose fromat: (24/12)'))


def time_string(hours, minutes, time_format): 
    
    if time_format == 12:
        if hours > 12:
            hours= hours - 12
            print(f'the time is now {hours, minutes} in format 12')
        else:
            hours=hours
            print(f'the time is now {hours, minutes} in format 12')
    if time_format == 24:
        print(f'the time is now {hours, minutes} in format 24')

    return hours

time = int(time_string(hours, minutes, time_format))
print(f'the time is {time_format(time)}')