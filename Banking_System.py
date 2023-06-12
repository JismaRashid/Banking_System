"""
Write a python program to replicate a Banking system. The following features
are mandatory:
1.Account login
2. Amount Depositing
3. Amount Withdrawal

"""

class Bank:
    def __init__(self,ac_no,name,balance=0):

        self.ac_no=ac_no
        self.name=name
        self.balance=balance

    def login(self,enterd_ac_no,entered_name):
        if self.ac_no==enterd_ac_no and self.name==entered_name:
            print("Login successful.\nWelcome to Banking System")
            while True:
                print("1.Deposite\n2.Withdraw\n3.Exit")
                choice = int(input("Enter your choice : "))
                if choice == 1:
                    user.deposit()
                elif choice == 2:
                    user.withdraw()
                elif choice == 3:
                    print("Thank you for using our banking system.")
                    break
                else:
                    print("Invalid option")

        else:
            print("Login failed.")

    def deposit(self):
        amt=float(input("Enter the amount to deposit : "))
        self.balance+=amt
        print(amt," credited to your account.final balance : ",self.balance)

    def withdraw(self):
        amt=float(input("Enter the amount to withdraw : "))
        if self.balance>=amt:
            self.balance-=amt
            print(amt," debited from your account.final balance : ",self.balance)
        else:
            print("Insufficient Balance.Current balance : ",self.balance)
user_details={"101":"Anu","102":"Manu","103":"Sonu"}

enterd_ac_no=input("enter your Account Number : ")
entered_name=input("enter your name : ")

if enterd_ac_no in user_details:
    user=Bank(enterd_ac_no,user_details[enterd_ac_no])
    user.login(enterd_ac_no,entered_name)
else:
    print("Account not found")

