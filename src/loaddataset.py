import json
from pymongo import MongoClient
from os import environ
from bson.objectid import ObjectId


def load_dataset():
    # Making Connection
    mongo_uri = environ.get("MONGO_URI")
    client = MongoClient(mongo_uri)
    
    # database
    db = client["restaurant"]
    
    # Created or Switched to collection
    Collection = db["restaurant"]


    if Collection.count_documents({}) == 0:
        # Loading or Opening the json file
        with open('/the-real-devops-challenge/data/restaurant.json') as file:
            for jsonobjs in file:
                file_data = json.loads(jsonobjs)
                oldid = file_data["_id"]['$oid']
                objInstance = ObjectId(oldid)
                file_data["_id"] = objInstance
                print(file_data)

                Collection.insert_one(file_data)