"""
Menu-Based Order System

Author: Abinash Prasana

This script displays a menu of food items with prices,
lets users select items, and calculates the total order value.
"""

# Food menu with prices
menu = {
    "pizza": 3.5, "nachos": 4.50, "popcorn": 6.6,
    "fries": 2.50, "chips": 1.5, "pretzel": 4.4,
    "soda": 2.50, "lemonade": 5.55
}

cart = []
total = 0

# Display menu
print("---------------- Menu ----------------")
for item, price in menu.items():
    print(f"{item:10} : ${price:.2f}")
print("--------------------------------------")

# Take user input
while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif food in menu:
        cart.append(food)
    else:
        print("Item not found in menu.")

# Print order summary
print("\n------------- Your Order -------------")
for food in cart:
    total += menu[food]
    print(food, end=" ")

print(f"\nTotal cart: ${total:.2f}")