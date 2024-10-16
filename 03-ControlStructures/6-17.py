hour = int(input('insert the hour using 24 format: '))
min = (input('insert the minutes'))

if hour > 12:
    hour-=12
    print(f'the time is {hour}:{min} in 12h format')
else:
    print(f'time time is {hour}:{min}')