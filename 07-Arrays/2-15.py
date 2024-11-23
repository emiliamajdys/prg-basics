car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
bank_transactions = [-150, -20, 300, -45, -60, 500, -120]

# Get the length of the list
n = len(car_fuel_consumption)

# Bubble sort algorithm to sort the car_fuel_consumption list in ascending order
for i in range(n):  # Loop over the entire list
    for j in range(n - i - 1):  # Inner loop for comparisons
        if car_fuel_consumption[j] > car_fuel_consumption[j + 1]:  # Compare adjacent items
            # Swap if the current item is greater than the next item
            car_fuel_consumption[j], car_fuel_consumption[j + 1] = car_fuel_consumption[j + 1], car_fuel_consumption[j]

# Print the sorted fuel consumption list
print(car_fuel_consumption)

z = len(bank_transactions)

# Bubble sort algorithm to sort the car_fuel_consumption list in ascending order
for i in range(z):  # Loop over the entire list
    for j in range(z - i - 1):  # Inner loop for comparisons
        if bank_transactions[j] > bank_transactions[j + 1]:  # Compare adjacent items
            # Swap if the current item is greater than the next item
           bank_transactions[j], bank_transactions[j + 1] = bank_transactions[j + 1], bank_transactions[j]

# Print the sorted fuel consumption list
print(bank_transactions)

