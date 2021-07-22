from pymongo import MongoClient
import pymongo
from dbConnect import connectScrape
import sys, os
sys.path.append(os.path.abspath(os.path.join('..','routes')))
import time
import concurrent.futures
import requests
import os
from getUserPosts import userPosts

def addUserPostsFunc():
    users = userPosts()
    db = connectScrape('TikScrape')
    counter = 0

    def findAndUpdate(user):
        db.TokFl.find_one_and_update({"user.sec_uid": user["aweme_list"][0]["sec_uid"]}, {"$set":{"userPosts":user}})
        counter+=1
        return counter
        

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_to_url = (executor.submit(findAndUpdate, querystring)for user in users)
        time1 = time.time()
        for future in concurrent.futures.as_completed(future_to_url):
            try:
                data = future.result()
                print(data)
            except Exception as exc:
                data1 = str(type(exc))
                print(exc)
            finally:
                print("Working!")
                

        time2 = time.time()
    #print(f'Took {time2-time1:.2f} s')
    print("Done updating"+str(counter)+"documents!")