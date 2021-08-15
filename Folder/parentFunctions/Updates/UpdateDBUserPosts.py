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
    db = connect("TikScrape")

    secUids = findSecUid()
    print(len(secUids))
    subset = []
    counter = 0
    test = []
    z = 0
s
    for x in secUids:
        if z>20372:
            test.append(x)
        z+=1
    print("number of users from DB to be updated for POSTS is:"+str(len(test)))
    #gets documents from how many we want to scrape
    i = 0
    for x in test:
        counter+=1
        subset.append(x)
        if i % 200 == 0:
            users = userPosts(subset)
            print("Length of POSTS after API is:"+str(len(users)))
            print(str(counter)+" POSTS have been updated so far!") 
            with concurrent.futures.ThreadPoolExecutor(max_workers=200) as executor:
                future_to_url = (executor.submit(findAndUpdateUserPosts, db, user)for user in users)
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

    print("The Whole DBs POSTS are up to date...")