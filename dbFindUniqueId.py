from pymongo import MongoClient
import time

from Folder.db.dbConnect import connect


def findSecUid():
    db = connect("TikScrape")
    #gets all users from the db list above^ and then only shows the sec_uid to reference user
    cursor = db.TokFl.find({})
    cursor = db.TokFl.aggregate([{'$project':{ 'user.sec_uid':1, '_id':0,}}])

    #adding sec_uids to one giant list to then be used  later for reference
    user_id = []
    for document in cursor:
        try:
            print(document)
            user_id.append(document['user']['sec_uid'])
            print("working SECUID", end="\n\n\n\n\n")
            print(document['user']['sec_uid'])
 
        except KeyError: 
            print(KeyError)
            print("not working")
	        # handle the error 
        
            
    print(user_id)
    return user_id