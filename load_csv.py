import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient


client=MongoClient('mongodb+srv:')

db = client.API
collection = db.kaggle

csvfile = open('ford.csv', 'r')
reader = csv.DictReader( csvfile )
header= [ "model", "year", "price", "transmission","mileage", "fuelType","tax","mpg","engineSize"]
for each in reader:
    row={}
    for field in header:
        row[field]=each[field]
    collection.insert(row)