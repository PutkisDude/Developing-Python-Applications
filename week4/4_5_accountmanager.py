#Author Lauri Putkonen
#Account manager with menu:
#User can make deposits
#Do withdrawal
#Check the balance

import sys

#Deposit to account
def deposit(deposit_amount):
    global balance
    if deposit_amount < 0:
        print("Can't deposit negative amount")
    else:
        balance += deposit_amount
        account_balance()

            
#Withdraw from account
def withdraw(withdraw_amount):
    global balance
    if balance < withdraw_amount:
        print("Balance is too low")
    elif withdraw_amount < 0.05:
        print("Too low amount to withdraw")
    else:
        balance -= withdraw_amount
        account_balance()
        
# Check balance
def account_balance():
    global balance
    checkaccount = int(input("Do you want see account balance. \n1.Yes \n2.No\n"))
    if checkaccount == 1:
        print("Account balance is {:.2f}".format(balance))


balance = 4250.95

#Menu
print("ACTION MENU:\n\n1.Deposit \n2.Withdraw \n3.Check Balance \n4.Exit\n")

action = int(input("Choose action: "))

if action == 1:
    deposit_amount = float(input("Deposit amount: "))
    deposit(deposit_amount)
elif action == 2:
    withdraw_amount = float(input("Widthraw amount: "))
    withdraw(withdraw_amount)
elif action == 3:
    print("Account balance is", balance)
else:
    sys.exit(0)
