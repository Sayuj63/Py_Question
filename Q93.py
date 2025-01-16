class BankAccount:
    def __init__(self, owner, balance):
        self.__owner = owner  # Private attribute
        self.__balance = balance  # Private attribute

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid balance amount.")

    def display_owner(self):
        print(f"Account Owner: {self.__owner}")

account = BankAccount("Alice", 1000)
account.display_owner()
print(f"Balance: {account.get_balance()}")
account.set_balance(1200)
print(f"Updated Balance: {account.get_balance()}")
