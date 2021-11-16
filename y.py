from pymongo import MongoClient
import time

from Folder.db.dbConnect import connect

def findTags():
    print("Fining ids for users from db")
    db = connect("TikScrape")
    #gets all users from the db list above^ and then only shows the sec_uid to reference user
    cursor = db.TokFl.find({
         "Tag":{ "$exists": True}},{ 'Tag':1, '_id':0})
    #cursor = db.TokFl.aggregate([{'$project':{ 'TikTok.user.sec_uid':1, '_id':0,}}])

    #adding sec_uids to one giant list to then be used  later for reference
    user_id = []
    tags = []
    for document in cursor:
        try:
            for x in document["Tag"]:
                tags.append(x)
    
        except KeyError: 
            print(KeyError)
            print("not working")
	        # handle the error 
    
    #print(tags)
    tags = list(set(tags))
   # for i in tags:
    #    if i not in tags:
    #        res.append(i)
    return tags