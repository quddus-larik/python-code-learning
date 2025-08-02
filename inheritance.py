class CNIC:
    def __init__(self,number,linkedAcc):
        self.Number = number
        self.AccoutNumber = linkedAcc
    def data(self):
        print(f'your data cnic {self.Number} | {self.AccoutNumber}')

class Bank(CNIC):
    def __init__(self, number, linkedAcc, Name, BankName, amount, qty):
        super().__init__(number, linkedAcc)
        self.Name = Name
        self.Bank = BankName
        self.Amount = amount
        self.Qty = qty
    
    def showBank(self):
        print(f"bank name {self.Bank} | acc: {self.Number} | linked: {"CNIC: ", self.AccoutNumber}")

    def ShowBuyDATA(self):
        totalamount = self.Amount * self.Qty
        print("Total Amount ", totalamount)

quddus = Bank("03118923","5412","quddus","NBF",12000,3)
quddus.data()
quddus.showBank()
quddus.ShowBuyDATA()