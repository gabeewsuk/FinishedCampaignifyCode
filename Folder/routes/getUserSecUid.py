import concurrent.futures
import requests
import time
import sys, os
from pymongo import MongoClient
import pymongo
import os
from decouple import config


from Folder.db.Finders.dbFindSecUid import findSecUid
from Folder.db.Finders.dbFindUserId import findUserId

#get user by sec-uid... pulls all from db and gets data for each one
def getUser():
    out = []
    exceptions = []
    CONNECTIONS = 100
    TIMEOUT = 5
    querystrings = []

    user_ids = findSecUid()

    url = config("API_URL")+"/get-user"

    headers = {
    'x-rapidapi-key': config("API_KEY"),
    'x-rapidapi-host': config("API_HOST")
    }
    for x in user_ids:
        querystrings.append({"sec_user_id":str(x)})
        

    def load_url(querystring):
        response = requests.request("GET", url, headers=headers, params=querystring)
        time.sleep(1)
        if response.status_code == 429:
            print("API server is getting too many requests")
        return response.json()

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        future_to_url = (executor.submit(load_url, querystring)for querystring in querystrings)
        time1 = time.time()
        for future in concurrent.futures.as_completed(future_to_url):
            try:
                data = future.result()
                out.append(data)
            except Exception as exc:
                data1 = str(type(exc))
                print(exc)
            finally:
                time.sleep(3)

                

        time2 = time.time()
    print(f'Took {time2-time1:.2f} s')
    print(len(out))
    return out