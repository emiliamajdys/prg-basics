# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

# Function to calculate total number of seats
def seats_total():
    total_seats = 0
    for row in cinema_seats:
        total_seats += len(row)  # Each row has 5 seats
    return total_seats

# Function to calculate the number of available seats (A)
def seats_available():
    available_seats = 0
    for row in cinema_seats:
        available_seats += row.count('A')  # Count 'A' in each row
    return available_seats

# Function to calculate the number of booked seats (B)
def seats_booked():
    booked_seats = 0
    for row in cinema_seats:
        booked_seats += row.count('B')  # Count 'B' in each row
    return booked_seats

# Function to check the status of a specific seat
def seat_status(row, place):
    if cinema_seats[row-1][place-1] == 'A':
        return "Available"
    elif cinema_seats[row-1][place-1] == 'B':
        return "Booked"
    else:
        return "Invalid seat"

# Print cinema seating information
print('CINEMA INFORMATION TABLE')
print('Total seats:', seats_total())  # Calls the function to get total seats
print('Seats available:', seats_available())  # Calls the function to get available seats
print('Seats booked:', seats_booked())  # Calls the function to get booked seats

# Check specific seat statuses
print('Seat in row 1, place 1:', seat_status(1, 1))
print('Seat in row 5, place 5:', seat_status(5, 5))
print('Seat in row 3, place 5:', seat_status(3, 5))
