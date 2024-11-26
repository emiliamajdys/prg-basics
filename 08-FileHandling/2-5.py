# Creates a shopping list based on product names entered from the keyboard.

# Shopping list file name
shopping_list = 'shopping_list.txt'

# Adds a product name to the end of the shopping list
def add_product(file_name, product_name):
    with open(file_name, 'a') as file:  # 'a' mode ensures the file is created if it doesn't exist
        file.write(product_name + '\n')  # Write product name with a newline

# Takes product names from the keyboard and adds them to the shopping list
product = ""
while product != "0":
    product = input('Enter product name (0 stops): ')
    if product == "0":
        break
    else:
        add_product(shopping_list, product)  # Add product to shopping list
        print(f'Added: {product}')

print(f"Your shopping list has been saved to {shopping_list}.")

