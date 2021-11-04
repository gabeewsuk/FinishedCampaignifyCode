from pymongo import MongoClient
import time
import pymongo
import pandas as pd


from Folder.db.dbConnect import connect

def toDF(data):
# initialize list of lists
    # Create the pandas DataFrame
    df = pd.DataFrame(data, columns = ['instagram', 'TikTok', 'ins_followers', 'aViews', 'aLikes', 'aComments', 'tikFollowers', "InstaLink",  "TikTokLink"])
    
    # print dataframe.
    #print(df)
    df.to_csv('output.csv', index = False, header = True)


#find all SecUids in the db... Used for referencing scraping and updating
print("Fining ids for users from db")
db = connect("TikScrape")
#gets all users from the db list above^ and then only shows the sec_uid to reference user
#cursor = db.TokFl.find({{{ "$sort" : { "TikTok.user.follower_count" : -1 }},{"$and": [{ "TikTok.user.signature": { "$regex": "she/her", "$options": "i" }},
# {"TikTok.user.follower_count": { "$gt": 0, "$lt": 1000000 }}})



cursor = db.TokFl.find({
  
      "$or": [
        
         ##{ "Instagram.user.bio": { "$regex": ".com", "$options": "i" }},
          #{"Instagram.user.follower_count":{"$gt":20000}},
          {"Tag":{"$regex":"Roster"}},

        
        #{ "TikTok.user.signature": { "$regex": ".com", "$options": "i" }},
       
        #{ "TikTok.averages.superString": { "$regex": "#sponsored", "$options": "i" }},
        #{ "TikTok.user.signature": { "$regex": "👩‍❤️‍💋‍👩", "$options": "i" }},
        #{ "TikTok.user.signature": { "$regex": "🌈", "$options": "i" }},
        #{ "TikTok.user.signature": { "$regex": "👨‍❤️‍👨", "$options": "i" }}
      ],
      "$and": [
       #{ "country" : { '$nin': [
       # 'Portugal',
       # 'Spain']},
         { "Instagram.user.bio": { "$regex": "", "$options": "i" }},
         #{"TikTok.userPosts.aweme_list.0.general.desc":{ "$regex": "#fyp", "$options": "i" }},
          #{"TikTok.userPosts.aweme_list.0.general.date":{ "$gt":"2021-10-10T19:51:48.000+00:00"}},
         #"$gt":"2021-10-10T19:51:48.000+00:00"ç

          #{ "TikTok.user.signature": { "$regex": "@", "$options": "i" }},

       #{"TikTok.lastPostUpdate": {"$gt":"2021-09-27 02:58:56"}}
         #{ "TikTok.user.signature": { "$regex": ".com", "$options": "i" }},
        #{ "TikTok.averages.views": { "$gt": 75000, "$lt":25000000000}},
        #{"Instagram.user.follower_count":{"$lt":10000}},#,"$lt":1000000000000000}} ,
       # {"TikTok.userPosts.aweme_list.author.region": { "$regex": "US", "$options": "i" }}
        
      ],

    })
    
    
#cursor = cursor.sort("Instagram.user.follower_count", pymongo.ASCENDING)
          
#cursor = cursor.skip(500).limit(500);
          
          
          #{ { "TikTok.lastPostUpdate": { "$regex": "2021-10-08", "$options": "i" } })
#cursor = db.TokFl.aggregate([{'$project':{ 'TikTok.user.unique_id':1, "TikTok.averages.superString":1, '_id':0,}}])

#adding sec_uids to one giant list to then be used  later for reference
#search = []
#words = ["#bi", "lesbian", "gay",  '#lgbt', '#fyp', '#gay', '#xyz', 'trend', 'dirtbike', 'ski', 'blue', 'red', 
#'laser', 'chips', 'guac', 'salsa', 'dance', 'charlie', 'msu', 'potato', 'ratchet', 'zoom',  'covid', 'trump',  'crypto', 'walk', 'wop', 'wap', 'degenerate']
#time1 = time.time()
x= 0
data = []
sec_uids = []
for document in cursor:
  try:
    #f = []
    sec_uids.append(document["TikTok"]["user"]["sec_uid"])
    print("\n\n\n\n")
    instaLink = "https://www.instagram.com/"+str(document["TikTok"]["user"]["ins_id"])
    TTLink = "https://www.tiktok.com/@"+str(document["TikTok"]["user"]["unique_id"])+"?"

    f = [document["TikTok"]["user"]["ins_id"], document["TikTok"]["user"]["unique_id"],
     document["Instagram"]["user"]["follower_count"], 
    document["TikTok"]["averages"]["views"], document["TikTok"]["averages"]["likes"], document["TikTok"]["averages"]["comments"],
    document["TikTok"]["user"]["follower_count"], instaLink, TTLink
    ]
    #print(ƒ)
    data.append(f)
    x+=1

    #insta, TT, ins_followers, aViews, aLikes, aComments, tikFollowers
    #print(document["Instagram"]["user"]["follower_count"])
    #print(document["TikTok"]["user"]["unique_id"])
    #print(document["TikTok"]["user"]["ins_id"])


  except:
    print("no instagram")
    #x+=1
  
    #try:
      #  for word in words:
      #      if word in document['TikTok']['averages']['superString']:
      #          search.append(document['TikTok']['user']['unique_id'])
    #except:
       # pass
#print(data)
toDF(data)
print(x)
print(sec_uids)
#time2 = time.time()
#print(time2-time1)
#print(len(search))
