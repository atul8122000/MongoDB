import pymongo

myclient = pymongo.MongoClient("mongodb+srv:")
mydb = myclient["gettingStarted"]
mycol = mydb["Copy_Collection"]

mydoc = mycol.find().sort("username")
print(mydoc)
for x in mydoc:
  print(x)