from pymongo import MongoClient
import pymongo
import time
import concurrent.futures
import requests
from decouple import config
from datetime import datetime as d



from Folder.routes.getUserPosts import userPosts
from Folder.db.dbConnect import connect
from Folder.db.findNUpdate.findNUpdateUserPosts import findAndUpdateUserPosts
from Folder.db.Finders.dbFindSecUid import findSecUid


#update all user posts in the db
def updateUserPosts():
    #get all data for posts and then sends them in for an update
    secUids = findSecUid()
    subset = []
    counter = 0
    i = 0
    for x in secUids:
        counter+=1
        subset.append(x)
        if i % 200 == 0:
            users = userPosts(subset)
            print("Length of documents after API is:"+str(len(users)))
            print(str(counter)+" have been updated so far!") 
            with concurrent.futures.ThreadPoolExecutor(max_workers=200) as executor:
                future_to_url = (executor.submit(findAndUpdateUserPosts, user)for user in users)
                time1 = time.time()
                for future in concurrent.futures.as_completed(future_to_url):
                    try:
                        data = future.result()
                    except Exception as exc:
                        print("Exception is:"+str(exc))
                    finally:
                        NAN = 0
                        

                time2 = time.time()
            print(f'Took {time2-time1:.2f} s')
            subset = []
        i+=1

    print("The Whole DBs Posts are up to date...")