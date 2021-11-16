from pymongo import MongoClient
import time
import pymongo
import pandas as pd
from datetime import datetime as d
import csv




from Folder.db.dbConnect import connect

def updateTag(Tag):
    with open('Roster.csv', 'r') as f:
        file = csv.reader(f)
        my_list = list(file)
    print(my_list)
    date = d.now()

    x  = 0
    print("Fining ids for users from db")
    db = connect("TikScrape")
    #gets all users from the db list above^ and then only shows the sec_uid to reference user##
    z = 0
    for x in my_list:
        x = str(x)
        x = x.replace("['", "")
        x = x.replace("']", "")
        print(x)
        try:
            db.TokFl.find_one_and_update({'TikTok.user.unique_id': x},
            { "$push": { "Tag": Tag } })
            z+=1


            
 
        except Exception as e: 
            print(e)
            print("not working")

    print(z)

        
    
