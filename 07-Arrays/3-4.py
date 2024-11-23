# Weekly meal plan [Breakfast, Lunch, Dinner] for 7 days
meal_plan = [
   ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],  # Monday
   ["Pancakes", "Sandwich", "Steak"],  # Tuesday
   ["Smoothie", "Chicken Wrap", "Salmon"],  # Wednesday
   ["Eggs", "Pasta", "Soup"],  # Thursday
   ["Toast", "Burrito", "Pizza"],  # Friday
   ["Cereal", "Salad", "Fish Tacos"],  # Saturday
   ["Bagel", "Rice and Beans", "Stir-fry"]  # Sunday
]

# Returns a week day name
def weekday(n):
   weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
   return weekdays[n-1]

# Returns a string with day meal names separated by commas
def day_meal_plan(meal_plan, day_number):
   # Get the meal plan for the given day_number (0-indexed for list)
   meal = meal_plan[day_number]
   day = weekday(day_number + 1)  # Get the weekday name using 1-based index
   return f"{day}: Breakfast - {meal[0]}, Lunch - {meal[1]}, Dinner - {meal[2]}"

# Prints weekly meal plan
def print_weekly_meal_plan(meal_plan):
    print("Weekly Meal Plan")
    print("-----------------")
    for i in range(7):  # Loop through 7 days (0-indexed)
        print(day_meal_plan(meal_plan, i))
    print("-----------------")

# Call the function to print the weekly meal plan
print_weekly_meal_plan(meal_plan)
