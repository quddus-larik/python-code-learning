class BankAcc:
    def __init__(self, balance, accNo, Name, PhNo):
        self.Balance = balance
        self.AccountNumber = accNo
        self.Name = Name
        self.Phone = PhNo

    def addAccount(self, Name, PhNo):  # Corrected method definition
        self.Name = Name
        self.Phone = PhNo
        print("Updated Name:", self.Name, "| Updated Phone:", self.Phone)

    def giveInfo(self):  # Added 'self' parameter
        print("Amount:", self.Balance, "| AccNO:", self.AccountNumber, "| Name:",self.Name,"| Phone", self.Phone)


# Creating and updating accounts
QuddusAcc = BankAcc(12000, 5231, "Quddus", 3231)
QuddusAcc.addAccount("Quddus", 9244)
QuddusAcc.giveInfo()

UmairAcc = BankAcc(45000, 21213, "Umair", 121)
UmairAcc.addAccount("Umair", 2411)
UmairAcc.giveInfo()
