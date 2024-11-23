# Prices of 10 products in the computer store (in currency units)
product_prices = [2999.99, 149.99, 499.99, 89.99, 1199.99, 349.99, 189.99, 99.99, 249.99, 999.99]

# Number of units available for each product
product_quantities = [5, 20, 10, 15, 7, 12, 25, 18, 9, 4]

# Calculate the total value of all goods available in the store
total_value = sum(price * quantity for price, quantity in zip(product_prices, product_quantities))

# Print the result
print(f"The total value of all goods available in the store is: {total_value:.2f} currency units")
