from dbConnect import connectScrape
from pymongo import MongoClient
import pymongo
import time

def findSecUid(x):
    db = connectScrape("TikScrape")
    cursor = db.TokFl.find({})
    for document in cursor:
          print(document)
    cursor = db.TokFl.aggregate([{'$project':{ 'user.sec_uid':1, '_id':0,}}])
    #cursor = db.TokFl.aggregate()
    user_id = []
    for document in cursor:
        try:
            print(document)
            user_id.append(document['user']['sec_uid'])
            print("working")
            print(document['user']['sec_uid'])
 
        except KeyError: 
            print(KeyError)
            print("not working")
	        # handle the error 
        
            
    print(user_id)
    time.sleep(2)
    return user_id