###
# House lighting with three bulbs and two switches
# Checking how many bulbs are illuminating the house
#
light_switch1 = False # False - switch off, True - switch on
light_switch2 = False
bulbs_on = 0
question1 = input('Do you want to turn on first switch: (T/N):')
if "T" == question1:
    bulbs_on += 1
    light_switch1 = True
question2 = input('Do you want to turn on second switch: (T/N):')
if "T"== question2:
    bulbs_on += 2
    light_switch2 = True

print(f"number of your bulbs are {bulbs_on} ")