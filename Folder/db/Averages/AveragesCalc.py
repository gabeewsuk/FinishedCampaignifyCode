from pymongo import MongoClient
import time



def averageCalc(cursor):
    print("COMMENTS")
    #averageComments = []
    #averageLikes = []
    #averageViews = []
    #averageShares = []
    #_ids = []
    Averages = []
    for document in cursor:
        totalComments = 0
        totalLikes = 0
        totalViews = 0
        totalShares = 0
        try:
            
            for x in range(6):
                totalComments += document['TikTok']['userPosts']['aweme_list'][x]['statistics']['comment_count']
            averageComments = round(totalComments/6)
            #averageComments.append(average)

            for x in range(6):
                totalLikes += document['TikTok']['userPosts']['aweme_list'][x]['statistics']['digg_count']
            averageLikes = round(totalLikes/6)
            #averageLikes.append(average)

            for x in range(6):
                totalViews += document['TikTok']['userPosts']['aweme_list'][x]['statistics']['play_count']
            averageViews = round(totalViews/6)
            #averageViews.append(average)

            for x in range(6):
                totalShares += document['TikTok']['userPosts']['aweme_list'][x]['statistics']['share_count']
            averageShares = round(totalShares/6)
            #averageShares.append(average)

            #_ids.append(docuement['_id'])
            averageList = []
            averageList.append(document['_id'])
            averageList.append(averageViews)
            averageList.append(averageLikes)
            averageList.append(averageComments)
            averageList.append(averageShares)
            Averages.append(averageList)

            
            print("Averages Working", end="\n\n\n\n\n")
        except KeyError: 
            print(KeyError)
            print("Averages not working for this"+str(document['_id']))
	        # handle the error 


        
            
    print(Averages)

    return Averages