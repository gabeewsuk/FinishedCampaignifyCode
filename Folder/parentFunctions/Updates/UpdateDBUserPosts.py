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

#update all user posts in the db
def updateUserPosts():
    #get all data for posts and then sends them in for an update
    users = userPosts() 

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_to_url = (executor.submit(findAndUpdateUserPosts, user)for user in users)
        time1 = time.time()
        for future in concurrent.futures.as_completed(future_to_url):
            try:
                data = future.result()
            except Exception as exc:
                print(exc)
            finally:
                print("--")
                

        time2 = time.time()
    print(f'Took {time2-time1:.2f} s')
    print("Done updating UserPosts!")