from pymongo import MongoClient
import pymongo
import certifi
import os
import ssl

def connectScrape(x):
    #client = pymongo.MongoClient(os.environ.get('MONGO_URI'), tlsCAFile=certifi.where())
    #client = pymongo.MongoClient(os.environ.get('MONGO_URI'),ssl_cert_reqs=ssl.CERT_NONE)
    client = pymongo.MongoClient(os.environ.get('MONGO_URI'))

    db = client[x]
    print(db.list_collection_names())

    print("connected to mongoDB!")
    return db
    

