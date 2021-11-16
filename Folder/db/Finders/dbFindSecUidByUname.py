from pymongo import MongoClient
import time

from Folder.db.dbConnect import connect

#find all SecUids in the db... Used for referencing scraping and updating
def findSecUidByUname(user_names):
    print("Fining ids for users from db")
    db = connect("TikScrape")
    sec_uids =  []
    for user in user_names:
        #gets all users from the db list above^ and then only shows the sec_uid to reference user
        cursor = db.TokFl.find({"TikTok.user.unique_id":user})


        #adding sec_uids to one giant list to then be used  later for reference
        for document in cursor:
            try:
                sec_uids.append(document['TikTok']['user']['sec_uid'])
                
    
            except KeyError: 
                print(KeyError)
                print("not working")
                print("dbFindSecUidByUname.py")
                # handle the error 
            
                
    return sec_uids