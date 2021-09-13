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
    db = connect('TikScrape')
    subset = []
    i = 0
    counter = 0
    print("number of users to add posts to is:"+str(len(userIds)))
    userCount = len(userIds)
    for x in userIds:
        counter+=1
        subset.append(x)
        if i % 200 == 0 or userCount < 200:
            users = userPostsUId(subset)
            print("Length of users being updated is"+str(len(users)))
            print(str(counter)+" have been updated so far!")
            with concurrent.futures.ThreadPoolExecutor(max_workers=500) as executor:
                future_to_url = (executor.submit(findAndUpdateUserPosts, db,  user)for user in users)
                time1 = time.time()
                for future in concurrent.futures.as_completed(future_to_url):
                    try:
                        data = future.result()
                    except Exception as exc:
                        print(exc)
                    finally:
                        NAN = 0

                time2 = time.time()
            print(f'Took {time2-time1:.2f} s')
            subset = []
        i+=1
        userCount-=1

    print("Done updating userPosts!")
