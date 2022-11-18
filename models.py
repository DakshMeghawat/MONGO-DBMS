class Stock():
    def __init__(self,name,sym,nos,value):
        self.name=name
        self.sym=sym
        self.nos=nos
        self.value=value

    #def getname():
     #   return (name)


class Marketpalce():
    def __init__(self,los):
        self.los=los

class User():
    def __init__(self,balance,Username,stocks_own):
        self.balance=balance
        self.Username=Username
        self.stocks_own=stocks_own
    def add_stocks(self,own):
        self.stocks_own.append(own)
g=Stock('apple','xyz','100','500')
f=Stock('apple','xyz','100','500')
S=User('APPLE','APL',[])

S.add_stocks(g)
S.add_stocks(f)
print(S.stocks_own[1].name)



        


