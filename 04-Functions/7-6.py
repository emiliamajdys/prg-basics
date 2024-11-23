def czy_binarna(liczba):
    # Sprawdzamy, czy liczba zawiera tylko znaki '0' lub '1'
    for cyfra in liczba:
        if cyfra not in ('0', '1'):
            return False
    return True
        
liczba = input('Insert the number: ')
final = czy_binarna(liczba)
print(final)
