from pymongo import MongoClient
import time

from Folder.db.dbConnect import connect

#find User Id, this is needed for pulling from the old db.. and updating users by username...
def findUserId(x):
    db = connect(x)
    print("Finding Users from hily influencers..")
    #gets all users from a specific previous list (old scraper lists) and then sends their ids for reference in return  statement 
    cursor = db.hilyinfluencers.find({})
    cursor = db.hilyinfluencers.aggregate([{'$project':{ 'authorMeta.id':1, '_id':0,}}])
    user_id = []
    for document in cursor:
        try:
            user_id.append(document['authorMeta']['id'])
           
 
        except KeyError: 
            print(KeyError)
            print(document)
        
    print(len(user_id))
    return user_id