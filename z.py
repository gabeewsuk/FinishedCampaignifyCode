from pymongo import MongoClient
import time
import pymongo
import pandas as pd
from datetime import datetime as d


from Folder.db.dbConnect import connect

def addEmailBio(Tag):
    


    date = d.now()

    x  = 0
    print("Fining ids for users from db")
    db = connect("TikScrape")
    #gets all users from the db list above^ and then only shows the sec_uid to reference user##
    cursor = db.TokFl.find("Tag":{ "$regex": Tag, "$options": "i" })
    counter1 = 0
    counter2 = 0
    counter3 = 0
    for document in cursor:
        try:
            data = document["TikTok"]["user"]["signature"]
            try:
                ins_data = document["Instagram"]["user"]["bio"]
            except:
                ins_data = "a b"
            tiktokEmail = ".com"
            instaEmail = "abc"
            bio = data.split()
            insBio = ins_data.split()
            for z in bio:
               
                if ("@" in z) and (".com" in z):
                    tiktokEmail = z
                    counter1+=1
                    print("Counter 1 is"+str(counter1))

            for word in insBio:
                if ("@" in word) and (".com" in word):
                    instaEmail = word
                    counter2+=1
                    print("Counter 2 is"+str(counter2))



                if(instaEmail != "abc"):
                    db.TokFl.find_one_and_update({'TikTok.user.unique_id': document['TikTok']['user']['unique_id']},
                    {"$set":
                    {
                    "instaBioEmail": instaEmail}})
                if(tiktokEmail != ".com"):
                    db.TokFl.find_one_and_update({'TikTok.user.unique_id': document['TikTok']['user']['unique_id']},
                    {"$set":
                    {
                    "tiktokBioEmail": tiktokEmail}})
                else:
                    counter3 +=1
        except Exception as e:
            print("not working "+str(e))
            pass

            
 
       

    print(counter1)
    print(counter2)
    print(counter3)

addEmailBio()
        
    
