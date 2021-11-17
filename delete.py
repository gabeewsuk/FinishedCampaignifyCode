from pymongo import MongoClient
import time
import pymongo
import pandas as pd
import datetime

from Folder.db.dbConnect import connect


print("Fining ids for users from db")
db = connect("TikScrape")

Tag = "GabeROA"
db.TokFl.delete_many(
{

    #"$or": [ 


        "Tag":{ "$regex": Tag, "$options": "i" },

        
        
    # ],
    # "$and": [
    #  { "Instagram": {"$exists":True}},
        #{ "Instagram.user.bio": { "$regex": "", "$options": "i" }},
    
        
    # ],

    }
    )
    
    
