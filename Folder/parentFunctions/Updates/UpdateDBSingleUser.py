from pymongo import MongoClient
import time
import concurrent.futures
import requests
from decouple import config

#Local File imports
from Folder.db.dbConnect import connect

def updateSingleUser(sec_uids):
    #setting variables
    querystrings = []
    querystringsPOSTS = []
    db = connect('TikScrape')
    headers = {
    'x-rapidapi-key': config("API_KEY"),
    'x-rapidapi-host': config("API_HOST")
    }

    #parsing through list and appending necessary elements to create querystrings for both posts and users
    for x in sec_uids:
        querystrings.append({"sec_user_id":str(x)})
        querystringsPOSTS.append({"sec_user_id":str(x),"count":"100", "max_cursor":"0"})
        
    #fetching user credentials
    def fetch_user(querystring):
        url = config("API_URL")+"/get-user"
        response = requests.request("GET", url, headers=headers, params=querystring)
        return response.json()

    #fetching user posts
    def fetch_user_posts(querstring):
        url = config("API_URL")+"/user-posts"
        response = requests.request("GET", url, headers=headers, params=querystring)
        return response.json()

    #--For all users sent in via array-- finding the user in Mongo and updating them with user creds first then updating posts $$(just replaced values for MVP)$$
    for querystring in querystrings:
        user = fetch_user(querystring)
        if user["user"] == None:
            print("This no longer exists")
        else:
            db.TokFl.find_one_and_update({'user.sec_uid': user["user"]["sec_uid"]}, {"$set":{"user":user["user"]}})
    for querystring in querystringsPOSTS:
        posts = fetch_user_posts(querystring)
        if posts["aweme_list"] == None:
            print("This user has no posts")
        else:
            db.TokFl.find_one_and_update({'user.user.sec_uid': posts["aweme_list"][0]["author"]["sec_uid"]}, {"$set":{"userPosts.aweme_list":posts["aweme_list"]}})
    

        
   
   