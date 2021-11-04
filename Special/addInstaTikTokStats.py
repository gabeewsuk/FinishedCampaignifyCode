from pymongo import MongoClient
import time

from Folder.db.dbConnect import connect

#aggregate the posts for each user in the db
db = connect("TikScrape")

def findMissingUserPosts():
    x  = 0
    print("Fining ids for users from db")
    db = connect("TikScrape")
    #gets all users from the db list above^ and then only shows the sec_uid to reference user##
    cursorlikeTT = db.TokFl.find( { 'TikTok.user.total_favorited': { '$exists': False } } )
    cursorfollowerTT = db.TokFl.find( { 'TikTok.user.follower_count': { '$exists': False } } )
    cursorviewsA = db.TokFl.find( { 'TikTok.averages.views': { '$exists': False } } )
    cursorlikesA = db.TokFl.find( { 'TikTok.averages.likes': { '$exists': False } } )
    cursorsharesA = db.TokFl.find( { 'TikTok.averages.shares': { '$exists': False } } )
    cursorcommentsA = db.TokFl.find( { 'TikTok.averages.comments': { '$exists': False } } )

    cursorlastUpdateTT = db.TokFl.find( { 'TikTok.lastUserUpdate.aweme_list': { '$exists': False } } )
    cursor = db.TokFl.find( { 'TikTok.userPosts': { '$exists': False } } )


    cursor = db.TokFl.find( { 'Instagram.user.follower_count': { '$exists': False } } )
    cursor = db.TokFl.find( { 'Instagram.postsAverages': { '$exists': False } } )
    cursor = db.TokFl.find( { 'Instagram.reelsAverages': { '$exists': False } } )
    cursor = db.TokFl.find( { 'Instagram.reelsPosts': { '$exists': False } } )
    cursor = db.TokFl.find( { 'Instagram.feedPosts': { '$exists': False } } )





    print(":")
    user_id = []
    x = 0
    for document in cursor:##
        print(x)
        x+=1
        try:
            user_id.append(document['TikTok']['user']['sec_uid'])
            
 
        except KeyError: 
            print(KeyError)
            print("not working")
	        # handle the error 
        
    print(len(user_id))
    return user_id
findMissingUserPosts()