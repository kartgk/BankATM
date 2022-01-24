class Atm:
    def __init__ (self,cardNumber, Amount):
        self.cardNumber = cardNumber
        self.Amount = Amount
    def checkBalance(self):
        print('Your balance is ', self.Amount)

User = Atm(12345, 5000)
User.checkBalance()