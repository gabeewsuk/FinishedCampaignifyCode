from pymongo import MongoClient
#import sys, os
import time
import concurrent.futures
import requests
from decouple import config

from Folder.db.Finders.dbFindUserNames import findUserNames




#getUserId from an array of usernames
def getUserId(userNames):
    uNameList = findUserNames()
    print(len(uNameList))
    querystrings = []
    out = []
    trimName = []
    counter = 0
    for x in userNames:
        if x not in uNameList:
            counter +=1
            trimName.append(x)
    #print(trimName)
    print(len(trimName))

     
            

    url = config("API_URL")+"/username-to-id"


    headers = {
        'x-rapidapi-key': config("API_KEY"),
        'x-rapidapi-host': config("API_HOST")
        }



    #for x in trimName:
       # querystrings.append({"username":str(x)})
    #trimUname = []
    #for querystring in querystrings:
    #    new = querystring["username"]
     #   new = new.replace("{'username': '", "")
    #    new = new.replace("'}", "")
    #    trimUname.append(new)
    #print(trimUname)
    #uniqueList = []
    #for x in trimUname:
    #    if new in uNameList:
    #        print("name already in list")
    #    else:
    #        uniqueList.append(x)
    #        
    #print(uniqueList)
    def load_url(new):
        response = requests.request("GET", url, headers=headers, params={"username":new})
        while response.status_code == 429:
            print("API server is getting too many requests")
            time.sleep(4)
            response = requests.request("GET", url, headers=headers, params={"username":new})
        return response.json()

    with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
        future_to_url = (executor.submit(load_url, Uname)for Uname in trimName)
        time1 = time.time()
        time4 = time.time()
        for future in concurrent.futures.as_completed(future_to_url):
            try:
                data = future.result()
                if data == 0:
                    print("user already in DB")
                else:
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
            user_id.append(document['sec_uid'])
 
        except KeyError: 
            print(KeyError)
            print("not working")
	        # handle the error 
        
    
    return user_id