import pymongo
myclient=pymongo.MongoClient("mongodb://localhost:27017/")

mydb=myclient["local"]
mycol=mydb["STOCK"]
#for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
for x in mycol.find({},{"user id": 0}):
    print(x)
#x=mycol.find_one()
#print(x)