class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def display_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * (self.interest_rate / 100)

    # Method overriding
    def display_info(self):
        super().display_info()  # Call the display_info() method of the superclass
        print(f"Interest Rate: {self.interest_rate}%")


# Usage of the BankAccount and SavingsAccount classes
bank_account = BankAccount("123456789", "John Doe", 1000)
bank_account.deposit(500)
bank_account.withdraw(200)
bank_account.display_info()

print("\n")

savings_account = SavingsAccount("987654321", "Jane Smith", 5000, 2.5)
savings_account.deposit(1000)
savings_account.withdraw(300)
savings_account.display_info()
print(f"Interest Earned: {savings_account.calculate_interest()}")
