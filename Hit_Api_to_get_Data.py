import requests
from pymongo import MongoClient


client = MongoClient('mongodb+srv:')

##– Create Database or Switch to Existing Database:
db = client.API

##– Create collection or Switch to Existing collection:
collection = db.Api_data


## Get Data From Rest API
url='https://www.courtlistener.com/api/rest/v3/dockets/'
response = requests.get(url)
res = response.json()
res= res["results"]
result = [dict(item,**{'_id':item['id']})for item in res]
collection.insert_many(result) 
