from pymongo import MongoClient
import pymongo
from dbConnect import connectScrape
import sys, os
#sys.path.append('../routes')
from scrapTikRequests import ScrapTikUser
import time


def bulkWriteUsers():
    documents = ScrapTikUser()
    db = connectScrape('TikScrape')
    db.TokFl.insert_many(documents)
    time.sleep(60)
    cursor = collection.find({})
    for document in cursor:
          print(document)


