from pymongo import MongoClient
import pymongo
import time
import concurrent.futures
import requests
from decouple import config
from datetime import datetime as d



from Folder.db.dbConnect import connect
from Folder.routes.getUserSecUid import getUser
from Folder.db.findNUpdate.findNUpdateUser import findAndUpdateUser

#updates all user profiles in the db
def updateUsers():
    db = connect("TikScrape")
    #get all data for users and then sends them in for an update
    users = getUser()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_to_url = (executor.submit(findAndUpdateUser,db, user)for user in users)
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
    print("Done updating Users!")