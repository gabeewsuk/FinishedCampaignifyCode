from pymongo import MongoClient
import pymongo
import time
import concurrent.futures
import requests
from decouple import config
from datetime import datetime as d
from Folder.db.Finders.dbFindAweme_List import findAweme_List
from Folder.db.dbConnect import connect
from Folder.db.Averages.AveragesCalc import averageCalc

def updateAvgs():
    db = connect('TikScrape')
    cursor = findAweme_List()
    Averages = averageCalc(cursor)
    def findAndUpdate(Average):
        date = d.now()
        db.TokFl.find_one_and_update({'_id': Average[0]}, 
        {"$set":{"TikTok.Averages.views":Average[1],
        "TikTok.Averages.likes":Average[2],
        "TikTok.Averages.comments":Average[3],
        "TikTok.Averages.shares":Average[4],
        "TikTok.Averages.lastAverageUpdate":date.strftime("%Y-%m-%d %H:%M:%S")}})
        return Average[0]
   
    with concurrent.futures.ThreadPoolExecutor(max_workers=500) as executor:
        future_to_url = (executor.submit(findAndUpdate, Average)for Average in Averages)
        time1 = time.time()
        for future in concurrent.futures.as_completed(future_to_url):
            try:
                data = future.result()
                print(data)
            except Exception as exc:
                print(exc)
            finally:
                print("updating averages...")
                

        time2 = time.time()
    print("Done updating Averages!")