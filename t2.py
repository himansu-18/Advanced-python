global balance
balance = 0
transaction = []
def deposit():
        amount = int(input("Enter The Amount"))
        global balance  
        balance = balance+amount
        transaction.append(amount)
        print("amount deposited")
        

def withdraw():
    amount = int(input("Enter the withdraw amount"))
    global balance
    if(balance>amount):
        balance = balance-amount
    else:
        print("Insufficient Balance")
        
def check_bal():
    print("Your current balace is",balance)
def ext():
    exit()
while True:
    print("/n1.Deposite")
    print("/n2.Withdraw")
    print("/n3.Check Balance")
    print("/n4.Transaction")
    print("/n5.Exit")
    choice = int(input("Enter your choice"))

    if(choice==1):
        deposit()
    elif(choice==2):
        withdraw()
    elif(choice==3):
        check_bal()
    elif(choice==5):
        ext()