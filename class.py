from models import Stock

class f:
    def __init__(self,balance,Username,stocks_own):
        self.balance=balance
        self.Username=Username
        self.stocks_own=stocks_own
    def add_stocks(self,own):
        
        self.stocks_own.append(own)

class l:
    def __init__(self,name,rol):
        self.name=name
        self.rol=rol
la=l('daksh',10)
lb=l('raj',20)
Sa=f
#Sa=f('APPLE','APL','1000')
Sa.add_stocks(la)
Sa.add_stocks(lb)
print(Sa.stocks_own)
