from pymongo import MongoClient
import time

from Folder.db.dbConnect import connect

#find all SecUids in the db... Used for referencing scraping and updating
def findSecUid():
    print("Fining ids for users from db")
    db = connect("TikScrape")
    #gets all users from the db list above^ and then only shows the sec_uid to reference user
    cursor = db.TokFl.find({})
    cursor = db.TokFl.aggregate([{'$project':{ 'TikTok.user.sec_uid':1, '_id':0,}}])

    #adding sec_uids to one giant list to then be used  later for reference
    user_id = []
    for document in cursor:
        try:
            user_id.append(document['TikTok']['user']['sec_uid'])
            
 
        except KeyError: 
            print(KeyError)
            print("not working")
	        # handle the error 
        
            
    return user_id