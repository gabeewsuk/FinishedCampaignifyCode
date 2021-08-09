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
        if z>150:
            test.append(x)
        z+=1
        if z == 1001:
            break
    print("number of users from DB is:"+str(len(test)))
    #gets documents from how many we want to scrape
    documents = scrapeUsers(test)

    print("Length of documents after API is:"+str(len(documents)))

    db = connect('TikScrape')

    with concurrent.futures.ThreadPoolExecutor(max_workers=500) as executor:
        future_to_url = (executor.submit(findAndUpdateUser, db, document)for document in documents)
        time1 = time.time()
        for future in concurrent.futures.as_completed(future_to_url):
            try:
                data = future.result()
                print(data)
            except Exception as exc:
                print("Exception is:"+str(exc))
            finally:
                x = 0
                

        time2 = time.time()
    print(f'Took {time2-time1:.2f} s')
    print("bulk insert users complete...")
    return test
    


