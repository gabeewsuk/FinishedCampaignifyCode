from pymongo import MongoClient
import time
import pymongo
import pandas as pd
from datetime import datetime as d


from Folder.db.dbConnect import connect

def updateSpecial():
    date = d.now()

    x  = 0
    print("Fining ids for users from db")
    db = connect("TikScrape")
    #gets all users from the db list above^ and then only shows the sec_uid to reference user##
    data = []
    cursor = db.TokFl.find({})
    x = 0
    for document in cursor:
        try:
            #insTiktokFollowerRate = document['Instagram']['user']['follower_count']/document['TikTok']['user']['follower_count']
            TikTokEngagementRate = document['TikTok']['averages']['views']/document['TikTok']['averages']['likes']
            db.TokFl.find_one_and_update({'TikTok.user.unique_id': document['TikTok']['user']['unique_id']},
            {"$set":
            {
            #"specialStats.insToTikTokRatio": insTiktokFollowerRate,
            "specialStats.TikTokEngagementRate": TikTokEngagementRate,
            "specialStats.lastUserUpdate":date.strftime("%Y-%m-%d %H:%M:%S")}},upsert = True)
            x+=1


            
 
        except Exception as e: 
            print(e)
            print("not working")

    print(x)

updateSpecial()
        
    
