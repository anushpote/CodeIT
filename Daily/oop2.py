# OOP Continued:

class BankAccount:
    def __init__(self, account_name, balance=0):
        self.account_name = account_name
        self.balance = balance

account1 = BankAccount("Ram", 15000)
account2 = BankAccount("Shyam")

print("Balance of account1", account1.balance)
print("Balance of account2", account2.balance)