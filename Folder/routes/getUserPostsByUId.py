import concurrent.futures
import requests
import time
from pymongo import MongoClient
import pymongo
from decouple import config


#get user posts by User id... Needed for when we add users by username
def userPostsUId(userIds):
    out = []
    exceptions = []
    CONNECTIONS = 100
    TIMEOUT = 5
    querystrings = []



    url = config("API_URL")+"/user-posts"
    headers = {
    'x-rapidapi-key': config("API_KEY"),
    'x-rapidapi-host': config("API_HOST")
    }


    z = 0
    for x in userIds:
        querystrings.append({"user_id":str(x),"count":"32", "max_cursor":"0"})


    def load_url(querystring):
        x = 0
        response = requests.request("GET", url, headers=headers, params=querystring)
        while response.status_code == 429:
            print("API server is getting too many requests"+str(x))
            time.sleep(4)
            response = requests.request("GET", url, headers=headers, params=querystring)
            print("NEW STATUS CODE:"+str(response.status_code))
            x+=1
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
                time2 = time.time()
                print(f' reqest Took {time2-time1:.2f} s')

                
    print(f' average request took {(time2-time1)/len(out):.2f} s')
    print(f'Took {time2-time1:.2f} s')
    print(len(out))
    return out