import concurrent.futures
import requests
import time
from pymongo import MongoClient
from decouple import config


#scrape users from api.. by Uids
def scrapeUsers(user_ids):
    out = []
    exceptions = []
    CONNECTIONS = 100
    TIMEOUT = 5
    querystrings = []
    average_time = 0


    url = config("API_URL")+"/get-user"

    headers = {
    'x-rapidapi-key': config("API_KEY"),
    'x-rapidapi-host': config("API_HOST")
    }

    #creating querystring for the request function
    for x in user_ids:
        querystrings.append({"user_id":str(x)})
        

    #request function
    def load_url(querystring):
        x = 0
        response = requests.request("GET", url, headers=headers, params=querystring)
        while response.status_code == 429:
            print("API server is getting too many requests"+str(x))
            time.sleep(3)
            response = requests.request("GET", url, headers=headers, params=querystring)
            print("NEW STATUS CODE:"+str(response.status_code))
            x+=1
        return response.json()

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        future_to_url = (executor.submit(load_url, querystring)for querystring in querystrings)
        time1 = time.time()
        time4 = time.time()
        for future in concurrent.futures.as_completed(future_to_url):
            time3 = time.time()
            try:
                data = future.result()
                out.append(data)
            except Exception as exc:
                print(exc)
            finally:
                time2 = time.time()
                if len(out) %10 ==0:
                    if (time2-time4) > 1.1:
                        print("TOO FAST")
                        time.sleep(1.5)
                    time4 = time.time()
                    
                print(len(out))
                average_time+=(time2-time3)
                print(f' reqest Took {time2-time1:.2f} s')

                

        time2 = time.time()
    print(f' average request took {(time2-time1)/len(out):.2f} s')
    print(f'Took {time2-time1:.2f} s')
    print(len(out))
    return out