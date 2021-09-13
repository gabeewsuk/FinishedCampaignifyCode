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
    db = connect('TikScrape')
    test = []
    counter = 0
    z = 0
    print("number of users from DB is:"+str(len(user_ids)))
    #gets documents from how many we want to scrape
    subset = []
    i = 0
    for x in user_ids:
        counter+=1
        subset.append(x)
        if len(user_ids)>5000:
            if i % 200 == 0:
                documents = scrapeUsers(subset)
                print("Length of documents after API is:"+str(len(documents)))
                print(str(counter)+" have been updated so far!")
                with concurrent.futures.ThreadPoolExecutor(max_workers=500) as executor:
                    future_to_url = (executor.submit(findAndUpdateUser, db, document)for document in documents)
                    time1 = time.time()
                    for future in concurrent.futures.as_completed(future_to_url):
                        try:
                            data = future.result()
                            #print(data)
                        except Exception as exc:
                            print("Exception is:"+str(exc))
                        finally:
                            NAN = 0
                            

                    time2 = time.time()
                print(f'Took {time2-time1:.2f} s')
                subset = []
        if len(user_ids)<20:
            documents = scrapeUsers(subset)
            print("Length of documents after API is:"+str(len(documents)))
            print(str(counter)+" have been updated so far!")
            with concurrent.futures.ThreadPoolExecutor(max_workers=500) as executor:
                future_to_url = (executor.submit(findAndUpdateUser, db, document)for document in documents)
                time1 = time.time()
                for future in concurrent.futures.as_completed(future_to_url):
                    try:
                        data = future.result()
                        #print(data)
                    except Exception as exc:
                        print("Exception is:"+str(exc))
                    finally:
                        NAN = 0
                        

                time2 = time.time()
            print(f'Took {time2-time1:.2f} s')
            subset = []


        if len(user_ids)>20 and len(user_ids)<500:
            if i % 10 == 0:
                documents = scrapeUsers(subset)
                print("Length of documents after API is:"+str(len(documents)))
                print(str(counter)+" have been updated so far!")
                with concurrent.futures.ThreadPoolExecutor(max_workers=500) as executor:
                    future_to_url = (executor.submit(findAndUpdateUser, db, document)for document in documents)
                    time1 = time.time()
                    for future in concurrent.futures.as_completed(future_to_url):
                        try:
                            data = future.result()
                            #print(data)
                        except Exception as exc:
                            print("Exception is:"+str(exc))
                        finally:
                            NAN = 0
                            

                    time2 = time.time()
                print(f'Took {time2-time1:.2f} s')
                subset = []

        if len(user_ids)>500 and len(user_ids)<1500:
            if i % 50 == 0:
                documents = scrapeUsers(subset)
                print("Length of documents after API is:"+str(len(documents)))
                print(str(counter)+" have been updated so far!")
                with concurrent.futures.ThreadPoolExecutor(max_workers=500) as executor:
                    future_to_url = (executor.submit(findAndUpdateUser, db, document)for document in documents)
                    time1 = time.time()
                    for future in concurrent.futures.as_completed(future_to_url):
                        try:
                            data = future.result()
                            #print(data)
                        except Exception as exc:
                            print("Exception is:"+str(exc))
                        finally:
                            NAN = 0
                            

                    time2 = time.time()
                print(f'Took {time2-time1:.2f} s')
                subset = []

        if len(user_ids)>1500 and len(user_ids)<5000:
            if i % 100 == 0:
                documents = scrapeUsers(subset)
                print("Length of documents after API is:"+str(len(documents)))
                print(str(counter)+" have been updated so far!")
                with concurrent.futures.ThreadPoolExecutor(max_workers=500) as executor:
                    future_to_url = (executor.submit(findAndUpdateUser, db, document)for document in documents)
                    time1 = time.time()
                    for future in concurrent.futures.as_completed(future_to_url):
                        try:
                            data = future.result()
                            #print(data)
                        except Exception as exc:
                            print("Exception is:"+str(exc))
                        finally:
                            NAN = 0
                            

                    time2 = time.time()
                print(f'Took {time2-time1:.2f} s')
                subset = []


        i+=1

    print("bulk insert users complete...")
    return test
    


