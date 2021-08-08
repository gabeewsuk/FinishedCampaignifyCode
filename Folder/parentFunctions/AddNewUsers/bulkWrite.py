from pymongo import MongoClient
import pymongo
import sys, os
import time
import concurrent.futures
from Folder.db.dbConnect import connect
from Folder.routes.getUser import scrapeUsers
from Folder.db.Finders.dbFindUserId import findUserId
from datetime import datetime as d
from Folder.db.findNUpdate.findNUpdateUser import findAndUpdateUser


#adds new users by user id
def addNewUsers(user_ids):
    test = []
    z = 0
    #choose how many users we want
    for x in user_ids:
        test.append(x)
        z+=1
        if z == 1001:
            break
    print("z is:"+str(len(test)))
    #gets documents from how many we want to scrape
    documents = scrapeUsers(test)
    
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=500) as executor:
        future_to_url = (executor.submit(findAndUpdateUser, document)for document in documents)
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
    print("bulk insert users complete...")
    return test
    


