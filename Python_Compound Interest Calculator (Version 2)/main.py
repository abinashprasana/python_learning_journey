"""
Compound Interest Calculator (Version 2)

Author: Abinash Prasana

This variation of the compound interest calculator uses while True loops
for input validation, ensuring that the principal, rate, and time values are non-negative.
"""

# Input validation for principal
while True:
    principal = float(input("Enter the principal amount: "))
    if principal < 0:
        print("Principal amount can't be less than zero.")
    else:
        break

# Input validation for interest rate
while True:
    rate = float(input("Enter the interest rate (%): "))
    if rate < 0:
        print("Interest rate can't be less than zero.")
    else:
        break

# Input validation for time
while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("Time can't be less than zero.")
    else:
        break

# Calculate compound interest
total = principal * pow((1 + rate / 100), time)
print(f"\nBalance after {time} years is ${total:.2f}")