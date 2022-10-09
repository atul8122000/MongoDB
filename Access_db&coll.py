from pymongo import MongoClient

client = MongoClient('mongodb+srv:')
print("connected")

##To get database
mydatabase = client.sample_airbnb


##To get Collection
mycollection = mydatabase.listingsAndReviews

##To get find data from collection
mycollection.find()