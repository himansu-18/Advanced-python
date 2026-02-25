# user  Function
def user():
    USERNAME = "admin"
    PASSWORD = "1234"
    attempts = 3

    while attempts > 0:
        user = input("Enter username: ")
        pwd = input("Enter password: ")

        if user == USERNAME and pwd == PASSWORD:
            print("\n user `verify   by6 Successful\n")
            return True  
        else:
            attempts -= 1
            print("Invalid credentials. Attempts left:", attempts)

    print("Too many failed attempts. Account locked.")
    return False


# Deposit Function
def deposit(balance, transactions):
    amt = int(input("Enter deposit amount: "))
    balance += amt
    transactions.append(("Deposit", amt))
    print("Amount deposited successfully.")
    return balance


# Withdraw Function
def withdraw(balance, transactions):
    amt = int(input("Enter withdraw amount: "))
    if balance >= amt:
        balance -= amt
        transactions.append(("Withdraw", amt))
        print("Amount withdrawn successfully.")
    else:
        print("Insufficient balance.")
    return balance


# Check Balance Function
def check_balance(balance):
    print("Your current balance is:", balance)


# Transaction History Function
def transactions(transactions):
    if not transactions:
        print("No transactions yet.")
    else:
        print("\nTransaction History:")
        for t in transactions:
            print(t[0], ":", t[1])


# Main Function
def main():
    balance = 0
    transactions = []

    if not user():
        return

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            balance = deposit(balance, transactions)
        elif choice == "2":
            balance = withdraw(balance, transactions)
        elif choice == "3":
            check_balance(balance)
        elif choice == "4":
            show_transactions(transactions)
        elif choice == "5":
            print("Thank you for using the system.")
            break
        else:
            print("Invalid choice. Try again.")


print("Welcome to the Bank Transaction System")
main()
