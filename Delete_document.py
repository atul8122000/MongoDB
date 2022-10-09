import pymongo

myclient = pymongo.MongoClient("mongodb+srv:")
mydb = myclient["gettingStarted"]
mycol = mydb["Copy_Collection"]

myquery = {"name":"Katherine David"}

mycol.delete_one(myquery)