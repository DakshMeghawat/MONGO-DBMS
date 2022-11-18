import json
from flask import Flask, redirect, url_for, request
import pymongo
import requests
#from models import Stock, User

app = Flask(__name__)


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
        stocks_own
    def add_stocks(self,own):
        self.stocks_own.append(own)
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["local"]

def InsertStockInMarket(stock):
    mycol=mydb["Marketplace"]
    #stock_json = json.dumps(stock.__dict__)
    #print(stock_json)
    x=mycol.insert_one(stock.__dict__)

def UpdateStockInMarket():
    None

def RemoveStockInMarket():
    None


@app.route("/instertstock", methods = ['POST'])
def InsertStockInMarketRoute():
    data = request.get_json()
    print(data)

    s_3=Stock(name=data['name'], sym=data['sym'], nos=data['nos'],value=data['value'])
    InsertStockInMarket(s_3)


    return data


@app.route("/test", methods=['POST'])
def test():
    return "<p>Hello, Anshu!</p>"

def main():
    pass
    #S_1=Stock("APPLE","APL",1000,10)
    
    #S_2=Stock("META","META",1000,20)
    #U_1=User(10000,"Daksh",[])
   # U_1.add_stocks(S_1)
    #U_1.add_stocks(S_2)

    #print(S_2.name)
    #print(U_1.stocks_own[0].name)

    #InsertStockInMarket(S_1)


if __name__=="__main__":
    main()

app.run(host='localhost', port=8080)

 