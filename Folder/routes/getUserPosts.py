import concurrent.futures
import requests
import time
from pymongo import MongoClient
import pymongo
from decouple import config

from Folder.db.Finders.dbFindSecUid import findSecUid
from Folder.db.Finders.dbFindUserId import findUserId

#get userPosts for all users in the db
def userPosts():
    out = []
    exceptions = []
    CONNECTIONS = 100
    TIMEOUT = 5
    querystrings = []

    #gets all secUids in mongodb
    secUids = findSecUid()


    url = config("API_URL")+"/user-posts"
    headers = {
    'x-rapidapi-key': config("API_KEY"),
    'x-rapidapi-host': config("API_HOST")
    }


    for x in secUids:
        querystrings.append({"sec_user_id":str(x),"count":"100", "max_cursor":"0"})


    def load_url(querystring):
        response = requests.request("GET", url, headers=headers, params=querystring)
        while response.status_code == 429:
            print("API server is getting too many requests")
            time.sleep(10)
            response = requests.request("GET", url, headers=headers, params=querystring)
        return response.json()

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        future_to_url = (executor.submit(load_url, querystring)for querystring in querystrings)
        time1 = time.time()
        time4 = time.time()
        for future in concurrent.futures.as_completed(future_to_url):
            try:
                data = future.result()
                out.append(data)
            except Exception as exc:
                data1 = str(type(exc))
                exceptions.append(data1)
                print(exc)
            finally:
                time2 = time.time()
                if len(out) %10 ==0:
                    if (time2-time4) > 1.1:
                        print("TOO FAST")
                        time.sleep(1.5)
                    time4 = time.time()
                    
                print(len(out))
                print(f' reqest Took {time2-time1:.2f} s')
    print(f' average request took {time2-time1/len(out):.2f} s')
    print(f'Took {time2-time1:.2f} s')
    print(len(out))
    return out