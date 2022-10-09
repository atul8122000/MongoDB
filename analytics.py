from pymongo import MongoClient

client = MongoClient('mongodb+srv:')


##To get database
mydatabase = client.sample_supplies

##To get Collection
mycollection = mydatabase.sales

##To get find data from collection

mydoc = mycollection.find({"purchaseMethod":"Online"}).count()