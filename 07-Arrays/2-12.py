categories = ["Food", "Transport", "Rent", "Entertainment"]
expenses = [500, 150, 1000, 200]

max_expense = max(expenses)  # Find the maximum expense
max_index = expenses.index(max_expense)  # Get the index of the maximum expense
max_category = categories[max_index]  # Get the category corresponding to that index

print(max_category, max_expense)
