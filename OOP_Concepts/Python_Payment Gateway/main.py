"""
Payment Processing System

Author: Abinash Prasana

This program demonstrates abstraction and polymorphism using Python's abc module.
It simulates a payment processing system where users can choose among different
payment methods like Credit Card, PayPal, or UPI.
"""

from abc import ABC, abstractmethod
class PaymentMethod(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass

class CreditCard(PaymentMethod):
    def make_payment(self, amount):
        print(f"Paid ₹{amount} using Credit Card")

class PayPal(PaymentMethod):
    def make_payment(self, amount):
        print(f"Paid ₹{amount} using PayPal")

class UPI(PaymentMethod):
    def make_payment(self, amount):
        print(f"Paid ₹{amount} using UPI")

def process_payment(method: PaymentMethod, amount: float):
    method.make_payment(amount)

def main():
    print("Choose your payment method:")
    print("*******************************")
    print("1. Credit Card\n2. PayPal\n3. UPI")
    print("*******************************")
    choose = input("Enter your choice(1-3): ")
    amount = float(input("Enter amount to pay: "))

    if choose == "1":
        method = CreditCard()
    elif choose == "2":
        method = PayPal()
    elif choose == "3":
        method = UPI()
    else:
        print("Invalid choice")
        return

    process_payment(method, amount)

if __name__ == "__main__":
    main()
