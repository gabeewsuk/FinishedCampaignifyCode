from pymongo import MongoClient
#import sys, os
import time
import concurrent.futures
import requests
from decouple import config




#getUserId from an array of usernames
def getUserId(userNames):
    querystrings = []
    out = []
        
    url = config("API_URL")+"/username-to-id"


    headers = {
        'x-rapidapi-key': config("API_KEY"),
        'x-rapidapi-host': config("API_HOST")
        }



    for x in userNames:
        querystrings.append({"username":str(x)})
        print(querystrings)
            
    print(querystrings)
    def load_url(querystring):
        new = querystring['username']["username"]
        print("querystring is:")
        print(new)
        response = requests.request("GET", url, headers=headers, params=new)
        while response.status_code == 429:
            print("API server is getting too many requests")
            time.sleep(4)
            response = requests.request("GET", url, headers=headers, params=new)
        return response.json()

    with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
        future_to_url = (executor.submit(load_url, querystring)for querystring in querystrings)
        time1 = time.time()
        time4 = time.time()
        for future in concurrent.futures.as_completed(future_to_url):
            try:
                data = future.result()
                out.append(data)
            except Exception as exc:
                data1 = str(type(exc))
                print(exc)
            finally:
                time2 = time.time()
                if len(out) %10 ==0:
                    if (time2-time4) < 3.3:
                        print("TOO FAST")
                        time.sleep(1.5)
                    time4 = time.time()
                    
                print(len(out))
                print(f' reqest Took {time2-time1:.2f} s')

                

        time2 = time.time()
    print(f'Took {time2-time1:.2f} s')
    print(len(out))
    print("getting user id from username")
    print(out)
    user_id = []
    for document in out:
        try:
            user_id.append(document['user_id'])
 
        except KeyError: 
            print(KeyError)
            print("not working")
	        # handle the error 
        
            
    return user_id