import random

acc_bal = 3000

def deposit():
    print(f'Your account balance is {acc_bal} \n Enter amount')
    deposit = float(input())

    if deposit != 0:
        current_bal = acc_bal + deposit
        print(f'Hello {first_name.capitalize()} your current Balance is {current_bal} . Transaction id is {random.random()} \nThank you for banking with ViviBank')
    else:
        print('Invalid input \n Try again')

def withdrawal():
    print(f'Your account balance is {acc_bal} \n Enter amount to withdraw')
    withdraw = float(input())

    if withdraw != 0: 
        current_bal = acc_bal - withdraw
        print(f'Hello {first_name.capitalize()} your current Balance is {current_bal}. Transaction id is {random.random()} \nThank you for banking with ViviBank')
    else:
        print('Invalid input \n Enter amount again')
        withdraw = float(input())

def banking():
    if first_name != '' and last_name != '':
        print('What transaction do you want to do? \n A. Deposit \n B. Withdrawal \n Enter the letter of the option you desire')
        option = input()
    else:
        print('You have not entered your name. Start again!')

    if option == 'a' or option == 'A':
        deposit()
       
    elif option == 'b' or option == 'B':
        withdrawal()

    else:
        print('Invalid input \n Try again')

print('Hello Welcome! Kindly enter your first name.')
first_name = input()
print('Enter your Surname')
last_name = input()

banking()

