"""
Compound Interest Calculator

Author: Abinash Prasana

This program calculates the compound interest based on user input:
- Principal amount
- Interest rate (annual)
- Time period (in years)

It ensures all input values are positive and then computes the final amount
using the formula: A = P * (1 + r/100)^t
"""

# Initialize inputs
principal = 0
rate = 0
time = 0

# Input validation for principal
while principal <= 0:
    principal = float(input("Enter the principal amount: "))
    if principal <= 0:
        print("Principal amount must be greater than zero.")

# Input validation for interest rate
while rate <= 0:
    rate = float(input("Enter the annual interest rate (%): "))
    if rate <= 0:
        print("Interest rate must be greater than zero.")

# Input validation for time
while time <= 0:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("Time must be greater than zero.")

# Calculate compound interest
total = principal * pow((1 + rate / 100), time)
print(f"\nBalance after {time} years is ${total:.2f}")