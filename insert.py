import pymongo

myclient = pymongo.MongoClient("mongodb+srv:")
mydb = myclient["gettingStarted"]
mycol = mydb["Copy_Collection"]

mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)