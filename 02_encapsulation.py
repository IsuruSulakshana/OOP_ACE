class BankAccount:
    def __init__(self, account_number,balance):
        self._account_number = account_number #protected
        self.__balance = balance #private
        
    def deposit(self, amount):
        self.__balance = self.__balance + amount
        self.__transaction_history("Deposit :",amount)
        
    def withdraw(self, amount):
        if (self.__balance - amount >= 1000):
            self.__balance = self.__balance - amount
            self.__transaction_history("Withdraw :",amount)
        else:
            print("Insufficient balance")
            
    def get_balance(self):
        return self.__balance
    
    def __transaction_history(self,type,amount):
        print(type,amount)

account = BankAccount("1234567",1000)

account.deposit(5000)
account.withdraw(2000)

balance = account.get_balance()
print(balance)
