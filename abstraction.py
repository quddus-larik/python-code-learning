from abc import ABC, abstractmethod

# Abstract Base Class
class BankAccount(ABC):
    def __init__(self, acc_holder, balance):
        self.acc_holder = acc_holder
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def show_balance(self):
        print(f"{self.acc_holder}'s Balance: Rs {self.balance}")

# Concrete Class 1
class SavingAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount
        print(f"Rs {amount} deposited to savings.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Rs {amount} withdrawn from savings.")
        else:
            print("Insufficient funds in savings.")

# Concrete Class 2
class CurrentAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount
        print(f"Rs {amount} deposited to current.")

    def withdraw(self, amount):
        # No balance check: allows overdraft
        self.balance -= amount
        print(f"Rs {amount} withdrawn from current.")

# Usage
quddus_saving = SavingAccount("Quddus", 10000)
quddus_saving.deposit(2000)
quddus_saving.withdraw(5000)
quddus_saving.show_balance()

umair_current = CurrentAccount("Umair", 5000)
umair_current.withdraw(7000)  # Allows overdraft
umair_current.show_balance()
