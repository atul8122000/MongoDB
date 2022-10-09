from pymongo import MongoClient
import datetime


client = MongoClient('mongodb+srv:')


#Create a new database on your cluster
db = client.gettingStarted

#Create a collection for your database.
people = db.people

# #document
# personDocument = {
#   "name": { "first": "Alan", "last": "Turing" },
#   "birth": datetime.datetime(1912, 6, 23),
#   "death": datetime.datetime(1954, 6, 7),
#   "contribs": [ "Turing machine", "Turing test", "Turingery" ],
#   "views": 1250000
# }
# #Insert the document into your collection
# people.insert_one(personDocument)

people.find_one({ "name.last": "Turing" })