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


def updateUsers():
    users = getUser()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_to_url = (executor.submit(findAndUpdateUser, user)for user in users)
        time1 = time.time()
        for future in concurrent.futures.as_completed(future_to_url):
            try:
                data = future.result()
                print(data)
            except Exception as exc:
                print(exc)
            finally:
                print("--")
                

        time2 = time.time()
    print("Done updating Users!")