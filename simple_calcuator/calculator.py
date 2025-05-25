"""
Simple Python Calculator

Author: Abinash Prasana

This script allows the user to perform basic arithmetic operations
(+ - * /) between two floating-point numbers entered via the terminal.
It validates the operator and handles division by zero.
"""

# Get operator from user
op = input("Enter an operator (+ - * /): ")

# Get two numbers from user
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

# Perform calculation based on operator
if op == "+":
    result = num1 + num2
    print(f"The result is {round(result, 2)}")
elif op == "-":
    result = num1 - num2
    print(f"The result is {round(result, 2)}")
elif op == "*":
    result = num1 * num2
    print(f"The result is {round(result, 2)}")
elif op == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"The result is {round(result, 2)}")
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid operator. Please enter one of (+ - * /).")