# Python mini project to demonstrate how OOP Encapsulation works.
# We used bank account as an example of encapsulation
# to protect data and methods from unauthorized access,
# and it can also make code more secure and easier to maintain.

class BankAccount:
    """This class represents a bank account.
    It has two attributes: account_number and balance.
    """
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    # We set deposit as a Methods
    # to protect data and methods from unauthorized access
    def deposit(self, amount):
        self.balance += amount

    # We set withdraw as another Methods
    # with error handling
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    # We set get_balance as another Methods
    def get_balance(self):
        # Format the balance with Euro symbol and comma separator
        formatted_balance = "€{:,}".format(self.balance)
        return formatted_balance

# We create a Bank Account as an object with the account number and balance
# and print its balance
initial_balance = 10000000
deposit_amount = 1123500
withdraw_amount = 78600

account = BankAccount("2443478692", initial_balance)

print("Initial balance: {}".format(account.get_balance()))

# We deposit $1,123,500
account.deposit(deposit_amount)

print("After deposit of €{:,.2f}: {}".format(deposit_amount, account.get_balance()))

# We withdraw $78,860
account.withdraw(withdraw_amount)

print("After withdrawal of €{:,.2f}: {}".format(withdraw_amount, account.get_balance()))


