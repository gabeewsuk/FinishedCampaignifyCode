from pymongo import MongoClient
import time

from Folder.db.dbConnect import connect

#aggregate the posts for each user in the db
def findAweme_List():
    db = connect("TikScrape")
    cursor = db.TokFl.find({})
    cursor = db.TokFl.aggregate([{'$project':{ 'TikTok.userPosts.aweme_list':1}}])
    return cursor