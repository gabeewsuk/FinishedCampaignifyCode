from pymongo import MongoClient
import time
import pymongo
import pandas as pd
from datetime import datetime as d


from Folder.db.dbConnect import connect

def updateTagScreenShot(Roster, Tag):

    date = d.now()

    x  = 0
    print("Fining ids for users from db")
    db = connect("TikScrape")
    z = 0
    for x in Roster:
        print(x)
        try:
            db.TokFl.find_one_and_update({'TikTok.user.unique_id': x},
            { "$push": { "Tag": Tag } })
            z+=1


            
 
        except Exception as e: 
            print(e)
            print("not working")

    print(z)

        
    
def readFile():
    with open('file.txt', 'r') as file:
        data = file.read()

        print(data)
    x = data.split()
    count = 0
    Arr = []
    for z in x:
        #if ("@" in z):
        if ("@" in z) and (z != "@") and (".com" not in z) and (len(z) != 2) and (z[0] == "@") and ("-" not in z):
            
            if z not in Arr:
                print(z)
                Arr.append(z)
                count+=1
    newArr = []
    for x in Arr:
        x = x.replace("@", "")
        newArr.append(x)
    
    return newArr





