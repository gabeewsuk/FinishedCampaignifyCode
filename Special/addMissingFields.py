#from pymongo import MongoClient
#import time

##from Folder.db.dbConnect import connect

#aggregate the posts for each user in the db
#db = connect("TikScrape")

#def findAweme_List():
 #   cursor = db.TokFl.find({})
 #   cursor = db.TokFl.aggregate([{'$project':{ 'TikTok.user':1, "TikTok.averages":1}}])
 #   return cursor
#def addInstaTikTokStats(cursor):
 #   for document in cursor:
 #       try:
    #        TTFollowers = document["TikTok"]["user"]["follower_count"]
  #          InstaFollowers = document["Instagram"]["user"]["followe_count"]
    #        Ratio = InstaFollowers/TTFollowers
    #        print(Ratio)
    #        user = document["TikTok"]["user"]["unique_id"]
    #        db.TokFl.find_one_and_update({'TikTok.user.sec_uid': user["user"]["sec_uid"]},
     #           {"$set":
     #           {"TikTok.user.avatar_thumb":user["user"]