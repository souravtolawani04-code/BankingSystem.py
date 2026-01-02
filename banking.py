#creating a banking system which give total money after debited and credited
class Account:
    def __init__(self,balance):
        self.balance = balance
        
    def debit(self,debit):
        self.balance -= debit
        print("after debited",debit ,"$money will be", self.balance)

    def credit(self,credit):
        self.balance += credit
        print("after crediting",credit, "$money will be", self.balance)   


acc = Account(30000)
acc.debit(2000)
acc.credit(23000)