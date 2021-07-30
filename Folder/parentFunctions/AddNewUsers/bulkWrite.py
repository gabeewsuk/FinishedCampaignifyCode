from pymongo import MongoClient
import pymongo
import sys, os
#sys.path.append('../routes')
from scrapTikRequests import ScrapTikUser
import time

from Folder.db.dbConnect import connect
from Folder.routes.getUser import scrapeUsers

def addNewUsers():
    documents = scrapeUsers()
    db = connect('TikScrape')
    db.TokFl.insert_many(documents)
    time.sleep(60)
    cursor = collection.find({})
    for document in cursor:
          print(document)


