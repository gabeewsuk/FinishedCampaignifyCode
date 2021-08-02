from pymongo import MongoClient
import time

from Folder.db.dbConnect import connect


def averageViews():
    db = connect("TikScrape")
    cursor = db.TokFl.find({})
    cursor = db.TokFl.aggregate([{'$project':{ 'TikTok.userPosts.aweme_list':1}}])

    averages = []
    for document in cursor:
        total = 0
        try:
            print(document['TikTok']['userPosts']['aweme_list'][0]['statistics'])
            for x in range(6):
                print(document['TikTok']['userPosts']['aweme_list'][x]['statistics']['play_count'])
                total += document['TikTok']['userPosts']['aweme_list'][x]['statistics']['play_count']
            print(total)
            average = (total/6)
            print(average)
            averages.append(average)
            print("working! Average Views", end="\n\n\n\n\n")
 
        except KeyError: 
            print(KeyError)
            print("Averages not working")
	        # handle the error 
        
            
    print(averages)
    return averages