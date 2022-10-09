from pymongo import MongoClient
from typing import Optional
import pymongo

Mongodb_url = 'mongodb+srv:'

source_mongo_db = "sample_analytics"
source_collection_name = "customers"

destination_mongo_db = "gettingStarted"
destination_collection_name = "Copy_Collection"


def get_collection(
        db_name: Optional[str] = None,
        mongo_url: Optional[str] = None,
        collection_name: Optional[str] = None
) -> pymongo.collection.Collection:
    """ Get a mongodb collection to write.
    Args:
    :param db_name:(str,optional): [description]07. Defaults to None.
    :param collection_name: (str,optional): [description]. Defaults to None.
    :param mongo_url: (str,optional): [description]. Defaults to None.
    
    Returns:
        pymongo.collection.Collection: [description]
    
    """
    client = pymongo.MongoClient(mongo_url)
    db = client[db_name]
    collection = db[collection_name]
    return collection

source_db = source_mongo_db
destination_db = destination_mongo_db
source_col = source_collection_name
destination_col = destination_collection_name


source_collection = get_collection(
    db_name = source_db,
    mongo_url = Mongodb_url,
    collection_name = source_col
)
source_collection_cursor = source_collection.find()

documents = [item for item in source_collection_cursor]

destination_collection = get_collection(
    db_name = destination_db,
    mongo_url = Mongodb_url,
    collection_name = destination_col
)

destination_collection.insert_many(documents)

print(f"INFO : Migration Done from {source_col} to {destination_col}")
