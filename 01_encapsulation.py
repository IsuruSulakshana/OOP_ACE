class BankAccount:
    def __init__(self, account_number,balance):
        self._account_number = account_number #protected
        self.__balance = balance #private
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        
    def withdraw(self, amount):
        if (self.balance - amount >= 1000):
            self.balance = self.balance - amount
        else:
            print("Insufficient balance")
    def get_balance(self):
        return self.__balance
    
account = BankAccount("1234567", 1000)

#print(account.__balance)
print(account.get_balance())
print(account._account_number)
