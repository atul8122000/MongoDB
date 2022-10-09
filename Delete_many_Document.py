import pymongo

myclient = pymongo.MongoClient("mongodb+srv:")
mydb = myclient["gettingStarted"]
mycol = mydb["Copy_Collection"]

myquery = { "address": {"$regex": "^S"} }

x = mycol.delete_many(myquery)

print(x.deleted_count, " documents deleted.")