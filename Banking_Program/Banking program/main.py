"""
Banking Program

Author: Abinash Prasana

This is a simple terminal-based banking simulation in Python.
It allows users to:
- View current balance
- Deposit money with input validation
- Withdraw money with overdraft protection
- Exit the session

Great for beginners learning about conditionals, functions, loops, and user input handling.
"""

# ===============================
# 🧾 Function: Show Balance
# ===============================
def show_balance(balance):
    print("**********************************")
    print(f"Your balance is {balance:.2f}")
    print("**********************************")
# ===============================
# 💰 Function: Deposit
# ===============================
def deposit():
    print("**********************************")
    amount = float(input("Enter amount to deposit: "))
    print("**********************************")
    if amount < 0:
        print("**********************************")
        print("That's not a valid amount.")
        print("**********************************")
        return 0
    else:
        print("**********************************")
        return amount
        print("**********************************")
# ===============================
# 💸 Function: Withdraw
# ===============================
def withdraw(balance):
    print("**********************************")
    amount = float(input("Enter amount to withdraw: "))
    print("**********************************")
    if amount > balance:
        print("**********************************")
        print("Insufficient funds.")
        print("**********************************")
        return 0
    elif amount < 0:
        print("**********************************")
        print("Amount must be greater than zero.")
        print("**********************************")
        return 0
    else:
        print("**********************************")
        return amount
        print("**********************************")
# ===============================
# 🏦 Main Program Loop
# ===============================
def main():
    balance = 0
    is_running =True
    while is_running:
        print("**********************************")
        print("\tWelcome to Banking Program")
        print("**********************************")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("**********************************")
        choice = input("Enter your choice: ")
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("**********************************")
            print("Invalid choice")
            print("**********************************")
    print("**********************************")
    print("Thank you for using Banking Program")
    print("**********************************")
# ===============================
# 🔁 Run the Script
# ===============================
if __name__ == '__main__':
    main()