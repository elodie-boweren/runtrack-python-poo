class Bank_account:
    def __init__(self, account_number, last_name, first_name, account_balance, overdraft= True ):
        self.__account_number = account_number
        self.__last_name = last_name
        self.__first_name = first_name
        self.__account_balance = account_balance
        self.__overdraft = True

    def display_info(self):
        print(f"Account holder: {self.__last_name} {self.__first_name}")
        print("Account number : ", self.__account_number)
    
    def display_balance(self):
        print(f"Current balance on account {self.__account_number} : {self.__account_balance} €")

    def get_account_number(self):
        return self.__account_number
    
    def get_account_number(self):
        return self.__account_number

    def deposit(self, amount):
        self.__account_balance += amount

    def withdraw(self, amount):
        if self.__account_balance > amount or self.__overdraft == True:
            self.__account_balance -= amount
            return self.__account_balance
        else: print("You have insufficient funds to make this withdrawal")

    def overdraft_charges(self):
        if self.__account_balance < 0:
            self.__overdraft_charges = self.__account_balance * 8 / 100
            self.__account_balance += self.__overdraft_charges
            print(f"Overdraft charges: {self.__overdraft_charges} €")   

    def transfer(self, __recipient, amount):
        if self.__overdraft == False:
            if amount > self.__account_balance:
                print("Funds insufficient to carry out tyransfer")
            else: self.__account_balance -= amount
            __recipient.__account_balance += amount
            print(f"You have transferred {amount}€ into account number {__recipient.get_account_number()}")
        if self.__overdraft == True:
            self.__account_balance -= amount
            __recipient.__account_balance += amount
            print(f"You have transferred {amount}€ into account number {__recipient.get_account_number()}")
    
account1 = Bank_account("B111", "Boweren", "Elodie", 582)
account1.display_info()
account1.display_balance()
# account1.deposit(300)
# account1.display_balance()
# account1.withdraw(600)
# account1.display_balance()
# account1.withdraw(600)
# account1.display_balance()

account1.withdraw(600)
account1.display_balance()
account1.overdraft_charges()
account1.display_balance()


account2 = Bank_account("U2153", "Lamouche", "Bertrand", -68, False)
account2.display_info()
account2.display_balance()

account1.transfer(account2, 200)

account2.transfer(account1,50)
account1.display_balance()
account2.display_balance()