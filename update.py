import pymongo

myclient = pymongo.MongoClient("mongodb+srv:")
mydb = myclient["gettingStarted"]
mycol = mydb["Copy_Collection"]

myquery = { "username": "valenciajennifer" }
newvalues = { "$set": { "username": "NewUser" } }

mycol.update_one(myquery, newvalues)

for x in mycol.find():
  print(x)