# create bank account class and store account holder ,balance and create method to display

class BankDetail:

    def __init__(self,account_holder,account_number,balance):
        self.account_holder=account_holder
        self.account_number=account_number
        self.balance=balance
    
    def DisplayDetail(self):
        print(f"Hi !! {self.account_holder} your account number is :{self.account_number} and total balance is: {self.balance}")

obj=BankDetail("Preety Gupta",20345689022,45000)
obj.DisplayDetail()                