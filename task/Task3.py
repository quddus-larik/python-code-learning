class bank_account:
    def __init__(self,acct_holder, balance):
        self.acct_holder = acct_holder
        self.balance = balance

    def get_balance(self):        
        return f"Current Balance : {self.balance}"


    def deposit(self,amount):
          self.balance += amount
          return f"Deposited : {amount}.New balance is {self.balance}"
      
    def withdraw(self,amount):
         if amount > self.balance :
              return "Amount is insufficient"
         else:
              self.balance -= amount
              return f"Withdraw : {amount}.New balance is {self.balance}"
      
   
# Creating An Account
holder = bank_account("Mike",40000)

print(holder.deposit(20000))
print(holder.withdraw(10000))
print(holder.get_balance())