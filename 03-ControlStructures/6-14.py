ig = input('do you have an ig account?:(y/n)')
tw = input('do you have an twitter account? (y/n)')
fb = input('do you have a fb account?: (y/n)')


if ig=="y" and tw=="y" and fb=="y":
    print('you are a good influencer!')
elif ig=="y" and tw=="y" and fb=="n":
    print('you are a good inffluencer!')
elif ig=="y" and tw=="n" and fb=="y":
     print('you are a good inffluencer!')
elif ig=="n" and tw=="y" and fb=="y":
    print("you are a good inluencer!")
else:
    print("you are not a good inlucener ;(")
