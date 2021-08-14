from pymongo import MongoClient
import time

from Folder.db.dbConnect import connect

#find all SecUids in the db... Used for referencing scraping and updating
def findMissingUserPosts():
    print("Fining ids for users from db")
    db = connect("TikScrape")
    #gets all users from the db list above^ and then only shows the sec_uid to reference user
    cursor = db.TokFl.find( { 'TikTok.userPosts': { '$exists': False } } )
    print(":")
    user_id = []
    x = 0
    for document in cursor:
        print(x)
        x+=1
        try:
            user_id.append(document['TikTok']['user']['sec_uid'])
            
 
        except KeyError: 
            print(KeyError)
            print("not working")
	        # handle the error 
        
    print(len(user_id))
    return user_id
findMissingUserPosts()