"""
Shopping Cart Calculator

Author: Abinash Prasana

This script allows users to build a simple shopping list.
It collects food items and their prices, displays them,
and calculates the total amount due.
"""

foods = []
prices = []
total = 0

# Collect user input until they quit
while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {food}: $"))
        foods.append(food)
        prices.append(price)

# Display the final cart
print("\n------- Your Cart --------")
for food in foods:
    print(food, end=" ")

# Calculate total
for price in prices:
    total += price

print(f"\nTotal price: ${total:.2f}")