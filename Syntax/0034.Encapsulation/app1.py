# Protected Members: with '_' character
# Private Members: with '__' characters

class BankAccount:
    def __init__(self, owner, balance, name):
        self.name = name          # public
        self._owner = owner       # protected
        self.__balance = balance  # private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit: {amount}")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdraw: {amount}")
        else:
            print("Not enough money!")

    # Getter:
    def get_balance(self):
        return self.__balance


account = BankAccount("Amir_404", 1000, "Amirhossein Emadi")
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)
print(account.get_balance())
# ---------------------------------------------------
# print(account._BankAccount__balance) -> is not recommended!
# print(account.__balance) -> AttributeError
