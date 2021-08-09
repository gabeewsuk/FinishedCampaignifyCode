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
        response = requests.request("GET", url, headers=headers, params=querystring)
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
                print(exc)
            finally:
                time.sleep(3)
                

        time2 = time.time()
    print(f'Took {time2-time1:.2f} s')
    print(len(out))
    return out