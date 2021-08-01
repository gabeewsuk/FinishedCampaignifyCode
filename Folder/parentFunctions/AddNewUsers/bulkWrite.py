from pymongo import MongoClient
import pymongo
import sys, os
#sys.path.append('../routes')
import time
import concurrent.futures
from Folder.db.dbConnect import connect
from Folder.routes.getUser import scrapeUsers
from Folder.db.Finders.dbFindUserId import findUserId
from datetime import datetime as d



def addNewUsers(user_ids):
    test = []
    z = 0
    for x in user_ids:
        test.append(x)
        z+=1
        if z == 5:
            break

    documents = scrapeUsers(user_ids)
    db = connect('TikScrape')


    def findAndUpdate(user):
        date = d.now()
        if user["user"] == None:
            print("This no longer exists")
        else:
            db.TokFl.find_one_and_update({'TikTok.user.sec_uid': user["user"]["sec_uid"]}, {"$set":{"TikTok.user":user["user"],"TikTok.lastUserUpdate":date.strftime("%Y-%m-%d %H:%M:%S")}},upsert = True)
        return user["user"]
        
   
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_to_url = (executor.submit(findAndUpdate, document)for document in documents)
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
    print("Done updating Users!")










    #db.TokFl.find_one_and_update({'user.sec_uid': user["user"]["sec_uid"]}, {"$set":{"user":user["user"]}})

    #db.TokFl.insert_many(documents)
    print("bulk insert users complete...")
    return test
    #time.sleep(60)
    #cursor = collection.find({})
    #for document in cursor:
     #     print(document)


