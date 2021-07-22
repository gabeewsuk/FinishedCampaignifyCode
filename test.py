from pymongo import MongoClient
import pymongo
import certifi
import os
import ssl


client = pymongo.MongoClient(os.environ.get('MONGO_URI'))

db = client['TikScrape']
print(db.list_collection_names())

print("connected to mongoDB!")