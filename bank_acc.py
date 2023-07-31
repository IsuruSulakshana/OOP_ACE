class BankAccount:
    bank_name = "MyBank"

    def __init__(self, account_number, balance, currency):
        self.account_number = account_number
        self.balance = balance
        self.currency = currency

    @staticmethod
    def is_valid_account_number(account_number):
        # Assuming a valid account number is a 10-digit number
        return isinstance(account_number, int) and len(str(account_number)) == 10

    @staticmethod
    def convert_currency(amount, from_currency, to_currency):
        # Simulated exchange rates (for demonstration purposes)
        exchange_rates = {
            "USD": 1.0,
            "EUR": 0.85,
            "GBP": 0.73,
        }

        if from_currency not in exchange_rates or to_currency not in exchange_rates:
            raise ValueError("Invalid currencies")

        return amount * exchange_rates[to_currency] / exchange_rates[from_currency]

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return amount
        else:
            print("Insufficient funds")
            return 0

    def __str__(self):
        return f"Account Number: {self.account_number}, Balance: {self.balance} {self.currency}"


# Using static attributes and methods
print("Bank Name:", BankAccount.bank_name)

account_number = 1234567890
if BankAccount.is_valid_account_number(account_number):
    account = BankAccount(account_number, 1000, "USD")
    print(account)
else:
    print("Invalid account number")

amount_to_convert = 500
converted_amount = BankAccount.convert_currency(amount_to_convert, "USD", "EUR")
print(f"{amount_to_convert} USD is approximately {converted_amount:.2f} EUR")
