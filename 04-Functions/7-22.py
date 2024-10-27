def is_six(code):
    if len(code)<6:
        return False
    if len(code) != len(set(code)):
        return False
    
    return True
    
    
password = input('insert the password: ')
final=is_six(password)
print(final)
