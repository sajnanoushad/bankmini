class User():
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.amount=0
        self.balance=0

    def deposit(self,amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("your current balance is :",self.balance ,"Rs")

    def withdraw(self,amount):
        self.amount = amount
        if self.amount>self.balance:
            print("Insufficient balance,your current balance is",self.balance,"Rs")
        else:
            self.balance = self.balance - self.amount
            print("your current balance is :",self.balance, "Rs")
    def show_details(self):
        print("Account holder details")
        print("Name :",self.name)
        print("Age :",self.age)


    def view_balance(self):
        self.show_details()
        print("your current balance is :",self.balance)

name = input("Enter your name:")
age = int(input("Enter your age :"))
a = User(name,age)
while True:
    print("\n 1. Deposit \n 2. Withdraw \n 3. Check Balance \n 4. Show Details \n 5. Quit")
    choice=int(input("Enter your choice"))
    if choice==1:
        amount=float(input("Enter amount to be deposit:"))
        a.deposit(amount)
    elif choice==2:
        amount=float(input("Enter amount to be withdraw:"))
        a.withdraw(amount)
    elif choice==3:
        a.view_balance()
    elif choice==4:
        a.show_details()
    elif choice==5:
        print("Exit")
        break
    else:
        print("You have to enter the wrong choice,Please enter the number between 1 to 5.")










