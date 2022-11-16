import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["local"]
mycol=mydb["STOCK"]

mydict={ "user id":"1234", "name":"rahul" , "stock":"APPLE"}
x=mycol.insert_one(mydict)

mydict={ "user id":"1234", "name":"sumit" , "stock":"GOOGLE"}
x=mycol.insert_one(mydict)
print(x.inserted_id)

