from pymongo import MongoClient
import time
import concurrent.futures
import requests
from datetime import datetime as d

from Folder.routes.getUserPostsByUId import userPostsUId
from Folder.db.dbConnect import connect
from Folder.db.findNUpdate.findNUpdateUserPosts import findAndUpdateUserPosts



#updates sent in users with user posts
def newUsers_addUserPosts(userIds):
    #gets the posts from the input
    users = userPostsUId(userIds)

    print("Length of users being updated is"+str(len(users)))
    db = connect('TikScrape')
    with concurrent.futures.ThreadPoolExecutor(max_workers=500) as executor:
        future_to_url = (executor.submit(findAndUpdateUserPosts, db,  user)for user in users)
        time1 = time.time()
        for future in concurrent.futures.as_completed(future_to_url):
            try:
                data = future.result()
            except Exception as exc:
                print(exc)
            finally:
                x = 0 

        time2 = time.time()
    print(f'Took {time2-time1:.2f} s')
    print("Done updating userPosts!")