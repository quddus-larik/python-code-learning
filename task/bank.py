class BankAccount:
    def __init__(self, AccHolder, Balance):
        self.accountHolder = AccHolder
        self.__Balance = Balance  

    def deposit(self, amount): 
        self.__Balance += amount

    def withdraw(self, amount):
        if amount < self.__Balance:
            self.__Balance -= amount   ## Mistake
        else:
            print("Insufficient Balance")

    def get_Balance(self):
        print(f'Balance on account of {self.accountHolder} is {self.__Balance}')

quddus = BankAccount("Quddus", 13000)
quddus.deposit(1000)
quddus.get_Balance()
quddus.withdraw(9000)
quddus.get_Balance()
