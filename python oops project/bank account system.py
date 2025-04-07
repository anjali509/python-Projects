class BankAccount:
    def __init__(self):
        self.account_holder=input("Enter account holder name :")
        self.account_number=int(input("Enter account number :"))
        self.__balance=int(input("Enter balance amount in account :"))

    def deposit(self,money):
        self.__balance=self.__balance+money
        print(f"Deposited {money}. New balance :{self.__balance}")

    def withdrawl(self,money):
        if money>self.__balance:
            print("Insufficient funds.....Not enough money for withdrawl")
        else:
            self.__balance=self.__balance-money
            print(f"Withdrawl {money}. New balance :{self.__balance}")

    def display(self):
        print(f"Account holder :{self.account_holder}")
        print(f"Account number :{self.account_number}")
        print(f"Balance :{self.__balance}")


p1=BankAccount()
print("------Account details---------")
p1.display()
print("------------------------")

while True:
    op=int(input('''Choose an option :
    1. Deposit
    2. Withdrawl
    3. Display
    4. Exit  '''))

    if op==1:
        amount=int(input("Enter amount to deposit :"))
        p1.deposit(amount)
    elif op==2:
        amount=int(input("Enter amoount to withdrawl :"))
        p1.withdrawl(amount)
    elif op==3:
        print("-----------------------------")
        p1.display()
        print("-----------------------------")
    elif op==4:
        break


