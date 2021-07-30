from pymongo import MongoClient
import time

from Folder.db.dbConnect import connect

def scrapeId(x):
    db = connect(x)

    #gets all users from a specific previous list (old scraper lists) and then sends their ids for reference in return  statement 
    cursor = db.influencers.find({})
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