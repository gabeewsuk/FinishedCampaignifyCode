from dbConnect import connectScrape
from pymongo import MongoClient
import pymongo
import time

def scrapeId(x):
    db = connectScrape(x)
    cursor = db.influencers.find({})
    for document in cursor:
          print(document)
    cursor = db.influencers.aggregate([{'$project':{ 'authorMeta.id':1, '_id':0,}}])
    user_id = []
    for document in cursor:
        try:
            user_id.append(document['authorMeta']['id'])
            print("working")
            print(document["authorMeta"]['id'])
 
        except KeyError: 
            print(KeyError)
	        # handle the error 
        
            
    print(user_id)
    time.sleep(20)
    return user_id