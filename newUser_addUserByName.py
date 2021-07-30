from pymongo import MongoClient
import pymongo
import sys, os
#sys.path.append('../routes')
from scrapTikRequests import ScrapTikUser
import time

from Folder.db.dbConnect import connect
from Folder.routes.getUser import scrapeUsers

def addNewUsers(userNames):
    #need a function here that gets the userNames sends them to tokfluence to get the sec_uid
    
    #need a function that takes the list of sec_uids then sends them in to scrape the user profiles

    db = connect('TikScrape')
    db.TokFl.insert_many(documents)
    time.sleep(60)
    cursor = collection.find({})
    for document in cursor:
          print(document)


