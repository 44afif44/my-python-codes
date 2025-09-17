class Bank_Account: 
    def __init__(self,account_holderr,account_numberr,balancee):
        self.account_holder=account_holderr
        self.account_number=account_numberr
        self.balance=balancee
    def display(self):
        print(f"account hlder={self.account_holder},account number={self.account_number},balance={self.balance}")
    def deposit(self):
        amount=float(input("Enter amount to be deposited: "))
        self.balance+=amount
        print(f"amount deposited:{amount}")
        print(f"New balance:{self.balance}")
    def withdraw(self):
        lamount=float(input("Enter amount to be withdrawn: "))
        if self.balance>=lamount:
            self.balance-=lamount
            print(f"amount withdrawn:{lamount}")
            print(f"New balance:{self.balance}")
        else:
            print("Insufficient balance")
customer1=Bank_Account("afif",666,50000)
customer2=Bank_Account("siam",777,60000)
customer1.display()
customer1.deposit()
customer1.withdraw()
customer2.display()
customer2.deposit()
customer2.withdraw()





