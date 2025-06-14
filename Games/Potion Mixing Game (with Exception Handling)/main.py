"""
Potion Mixing Game 🎮

Author: Abinash Prasana

A fun terminal-based fantasy game where users mix magical ingredients
to brew potions. It demonstrates:
- Input validation
- Built-in and custom exception handling
- Random success/failure
- Creative user interaction
"""

import random

# Custom exception for forbidden combinations
class ExplosionError(Exception):
    pass

# Ingredient list (capitalized)
ingredients = ["Unicorn Hair", "Dragon Scale", "Phoenix Feather", "Mermaid Tears", "Basilisk Venom"]
# Forbidden ingredient
forbidden_ingredient = "Basilisk Venom"

# Function to display available ingredients
def display_ingredients():
    print("\nAvailable Ingredients:")
    for index, item in enumerate(ingredients, start=1):
        print(f"{index}. {item}")

# Function to get valid input
def get_choice(prompt):
    while True:
        try:
            choice = int(input(prompt))
            if 1 <= choice <= len(ingredients):
                return ingredients[choice - 1]
            else:
                print("❌ Please enter a valid number from the list.")
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

# Main game logic
def mix_potion():
    print("🔮 Welcome to the Potion Mixing Game! 🔮")
    print("Choose two magical ingredients to create a potion.")
    print("But beware! One forbidden ingredient may cause an explosion... 💥")

    display_ingredients()

    ing1 = get_choice("Choose your first ingredient (1-5): ")
    ing2 = get_choice("Choose your second ingredient (1-5): ")

    print(f"\n🧪 Mixing {ing1} and {ing2}...")

    try:
        if ing1 == ing2:
            raise ValueError("⚠ You cannot mix the same ingredient twice!")

        if forbidden_ingredient in (ing1, ing2):
            raise ExplosionError("☠ That ingredient is too dangerous to use!")

        # Randomized success/failure
        if random.choice([True, False]):
            print("✅ Success! You've brewed a powerful potion!")
        else:
            print("😕 The potion fizzles... It didn't work as expected.")

    except ValueError as ve:
        print(f"Error: {ve}")
    except ExplosionError as ee:
        print(f"💣 Explosion: {ee}")

# Run the game
if __name__ == "__main__":
    mix_potion()