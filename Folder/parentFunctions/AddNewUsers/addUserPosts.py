from pymongo import MongoClient
#import sys, os
import time
import concurrent.futures
import requests
from datetime import datetime as d

from Folder.routes.getUserPostsByUId import userPostsUId
from Folder.db.dbConnect import connect
from Folder.db.findNUpdate.findNUpdateUserPosts import findAndUpdateUserPosts




def newUsers_addUserPosts(userIds):
    users = userPostsUId(userIds)
    with concurrent.futures.ThreadPoolExecutor(max_workers=500) as executor:
        future_to_url = (executor.submit(findAndUpdateUserPosts, user)for user in users)
        time1 = time.time()
        for future in concurrent.futures.as_completed(future_to_url):
            try:
                data = future.result()
                #print(data)
            except Exception as exc:
                print(exc)
            finally:
                print("--")
                

        time2 = time.time()
    #print(f'Took {time2-time1:.2f} s')
    print("Done updating documents!")