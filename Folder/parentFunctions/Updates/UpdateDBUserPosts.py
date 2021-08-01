from pymongo import MongoClient
import pymongo
import time
import concurrent.futures
import requests
from decouple import config
from datetime import datetime as d



from Folder.routes.getUserPosts import userPosts
from Folder.db.dbConnect import connect

def updateUserPosts():
    users = userPosts()
    db = connect('TikScrape')

    def findAndUpdate(user):
        date = d.now()
        if user["aweme_list"] == None:
            print("This user doesnt have posts")
        else:
            db.TokFl.find_one_and_update({'TikTok.user.sec_uid': user["aweme_list"][0]["author"]["sec_uid"]}, {"$set":{"TikTok.userPosts.aweme_list":user["aweme_list"],"TikTok.lastPostUpdate":date.strftime("%Y-%m-%d %H:%M:%S")}})

        return user["aweme_list"][0]["author"]["sec_uid"]
            
   
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_to_url = (executor.submit(findAndUpdate, user)for user in users)
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
    #print(f'Took {time2-time1:.2f} s')
    print("Done updating documents!")