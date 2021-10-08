from pymongo import MongoClient
import time

from Folder.db.dbConnect import connect

#find all SecUids in the db... Used for referencing scraping and updating
print("Fining ids for users from db")
db = connect("TikScrape")
#gets all users from the db list above^ and then only shows the sec_uid to reference user
cursor = db.TokFl.find({ "TikTok.lastPostUpdate": { "$regex": "-13", "$options": "i" } })
#cursor = db.TokFl.aggregate([{'$project':{ 'TikTok.user.unique_id':1, "TikTok.averages.superString":1, '_id':0,}}])

#adding sec_uids to one giant list to then be used  later for reference
#search = []
#words = ["#bi", "lesbian", "gay",  '#lgbt', '#fyp', '#gay', '#xyz', 'trend', 'dirtbike', 'ski', 'blue', 'red', 
#'laser', 'chips', 'guac', 'salsa', 'dance', 'charlie', 'msu', 'potato', 'ratchet', 'zoom',  'covid', 'trump',  'crypto', 'walk', 'wop', 'wap', 'degenerate']
#time1 = time.time()
x= 0
for document in cursor:
    print(document["TikTok"]["user"]["ins_id"])
    x+=1
    #try:
      #  for word in words:
      #      if word in document['TikTok']['averages']['superString']:
      #          search.append(document['TikTok']['user']['unique_id'])
    #except:
       # pass

print(x)
#time2 = time.time()
#print(time2-time1)
#print(len(search))
