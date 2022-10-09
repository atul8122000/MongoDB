from pymongo import MongoClient
import pandas as pd

client = MongoClient('mongodb+srv:')


db =client.API.Api_data
col =db.Api_data
Api_data_df = pd.DataFrame(col)
