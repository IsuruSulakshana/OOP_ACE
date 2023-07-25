class BankAccount:
    def __init__(self, account_number, balance = 1000) -> None:
        self.account_number = account_number
        self.balance = balance
       
    def deposit(self, amount):
        self.balance = self.balance + amount
        
    def withdraw(self, amount):
        if (self.balance - amount >= 1000):
            self.balance = self.balance - amount
        else:
            print("Insufficient balance")
            
    def display_balance(self):
        print("Account balance:", self.balance)
        
#creating objects of the BankAccount class
Account_A = BankAccount("223344556677", 5000)
Account_B = BankAccount("887766554433")

#Accessing Attributes & calling methods
Account_A.deposit(1000)
Account_A.display_balance()
Account_A.withdraw(5000)
Account_A.display_balance()
Account_A.deposit(2000)
Account_A.display_balance()
Account_A.withdraw(3000)
Account_B.display_balance()
