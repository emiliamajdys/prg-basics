car_speed = int(input('insert the speed :'))
speed_limit_min = 40
speed_limit_max = 140

if 140>car_speed >40:
    print(f'the speed {car_speed} is correct')
else: 
    print(f'the speed {car_speed} is too high, you have to slow down')