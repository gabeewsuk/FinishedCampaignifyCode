from pymongo import MongoClient
#import sys, os
import time
import concurrent.futures
import requests

from Folder.routes.getUserPosts import userPosts
from Folder.db.dbConnect import connect


def newUsers_addUserPosts():
    users = userPosts()
    db = connect('TikScrape')

    for user in users:
        #print(user.values())
        if user["aweme_list"] == None:    
            pass
        else:
            print(user["aweme_list"][0]["author"]["sec_uid"])
            print("\n\n\n")        

    def findAndUpdate(user):
        if user["aweme_list"] == None:
            print("This user doesnt have posts")
        else:
            db.TokFl.find_one_and_update({'user.sec_uid': user["aweme_list"][0]["author"]["sec_uid"]}, {"$set":{"userPosts":user}})
            #counter+=1
            print("updating"+str(counter))
            time.sleep(12)
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
    print("Done updating"+str(counter)+"documents!")