# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Initialize the total expenses for each category
food_total = 0
transport_total = 0
utilities_total = 0

# Initialize the weekly expenses list for each week
week_expenses = []

# Calculate weekly expenses and category totals
for week in monthly_expenses:
    week_food = week[0]  # Week's food expense
    week_transport = week[1]  # Week's transport expense
    week_utilities = week[2]  # Week's utilities expense
    
    # Add the weekly values to the total expenses
    food_total += week_food
    transport_total += week_transport
    utilities_total += week_utilities
    
    # Store weekly expenses for later printing
    week_expenses.append((week_food, week_transport, week_utilities))

# Print the monthly expenses and the breakdown by week
print('MONTHLY EXPENSES')
print('----------------')
print(f'Food: {food_total}')
print(f'Transport: {transport_total}')
print(f'Utilities: {utilities_total}')

# Print weekly expenses for each week
for i, (week_food, week_transport, week_utilities) in enumerate(week_expenses, start=1):
    print(f'Week {i}: Food: {week_food}, Transport: {week_transport}, Utilities: {week_utilities}')

# Print total expenses
print('---------------')
print(f'TOTAL: Food: {food_total}, Transport: {transport_total}, Utilities: {utilities_total}')
