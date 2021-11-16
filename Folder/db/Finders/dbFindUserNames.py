from pymongo import MongoClient
import time

from Folder.db.dbConnect import connect

#find all SecUids in the db... Used for referencing scraping and updating
def findUserNames():
    print("Fining usernames from DB")
    db = connect("TikScrape")
    #gets all users from the db list above^ and then only shows the sec_uid to reference user
    cursor = db.TokFl.find({})
    cursor = db.TokFl.aggregate([{'$project':{ 'TikTok.user.unique_id':1, '_id':0,}}])

    #adding sec_uids to one giant list to then be used  later for reference
    user_names = []
    for document in cursor:
        try:
            #user_names.append(document['TikTok']['user']['unique_id'])
            name = str(document["TikTok"]["user"]["unique_id"])
            #print(name)
            user_names.append(name)
            
 
        except KeyError: 
            pass
            #print(KeyError)
            #print("not working")
            #print("dbFindUserNames.py")
	        # handle the error 
        
            
    return user_names