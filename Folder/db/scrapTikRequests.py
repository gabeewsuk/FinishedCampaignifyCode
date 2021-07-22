import concurrent.futures
import requests
import time
import sys, os
sys.path.append(os.path.abspath(os.path.join('..','db')))
from dbFindUserId import scrapeId
from pymongo import MongoClient
import pymongo
import os

def ScrapTikUser():
    #print("SCRAPTIK REQUEST", end='\r')
    out = []
    exceptions = []
    CONNECTIONS = 100
    TIMEOUT = 5
    querystrings = []

    user_ids = scrapeId('influencer-database')


    url = os.environ.get("API_URL")
    
    headers = {
    'x-rapidapi-key': os.environ.get("API_KEY"),
    'x-rapidapi-host': os.environ.get("API_HOST")
    }
    z = 0
    for x in user_ids:
        querystrings.append({"user_id":str(x)})
        z+=1
        if z == 5:
            break
        

    def load_url(querystring):
        response = requests.request("GET", url, headers=headers, params=querystring)
        #sprint(response.json())
        return response.json()

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_to_url = (executor.submit(load_url, querystring)for querystring in querystrings)
        time1 = time.time()
        for future in concurrent.futures.as_completed(future_to_url):
            try:
                data = future.result()
                out.append(data)
                print(data)
            except Exception as exc:
                data1 = str(type(exc))
                exceptions.append(data1)
                print(exc)
            finally:
                #print(len(out),end="\r")
                print("Working!")
                #print(exceptions)
                

        time2 = time.time()
    #print(f'Took {time2-time1:.2f} s')
    print(len(out))
    return out