###
# Program that simulates the operation of an electronic thermometer.
#
temperature = int(input('insert the temp'))
if temperature > 35:
    print("It is extermely hot")
elif 35>temperature > 30:
    print("its hot")
elif 30>=temperature >= 15:
    print("its warm")
elif 15>temperature>=0:
    print("its cold")
elif temperature<0:
    print("warning, frost")