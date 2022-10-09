import pymongo

myclient = pymongo.MongoClient("mongodb+srv:")
mydb = myclient["gettingStarted"]
mycol = mydb["Copy_Collection"]

mydoc = mycol.find().limit(5)

for x in mydoc:
  print(x)