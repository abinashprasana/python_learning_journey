"""
Bank Account Management System

Author: Abinash Prasana

This Python program simulates a basic bank account system. It demonstrates the use of class-level variables,
class methods, static methods, and instance methods to manage user deposits and display bank policies.
"""

class BankAccount():
    total_accounts = 0

    def __init__(self,name, balance=0):
        self.name = name
        self.balance = balance
        BankAccount.total_accounts += 1

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.name} deposited ₹{amount}. New balance: ₹{self.balance}")

    @classmethod
    def get_total_accounts(cls):
        print(f"Total accounts created: {cls.total_accounts}")

    @staticmethod
    def bank_policy():
        print("Bank Policy: Minimum balance must be $500. Withdrawal limit: $25,0000/day")

BankAccount.bank_policy()

a1 = BankAccount("Abby", 500000)
a1.deposit(10000)

a2 = BankAccount("Lcuy", 500)
a2.deposit(10000)

BankAccount.get_total_accounts()