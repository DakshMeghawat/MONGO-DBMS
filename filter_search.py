import pymongo
myclient=pymongo.MongoClient("mongodb://localhost:27017/")

mydb=myclient["local"]
mycol=mydb["STOCK"]
myquery={"stock":"APPLE"}
mydoc=mycol.find(myquery)
for x in mydoc:
    print(x)