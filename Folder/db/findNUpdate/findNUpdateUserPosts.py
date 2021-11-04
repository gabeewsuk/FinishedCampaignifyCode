from Folder.db.dbConnect import connect
from datetime import datetime as d
from datetime import datetime

#Finding user and updating posts with correct trimmed schema
def findAndUpdateUserPosts(db, user):

    #setting initial variables
    date = d.now()
    counter = 0
    aweme_list = []
    userPosts = {}
    descSuperString = ''
    totalComments = 0
    totalLikes = 0
    totalViews = 0
    totalShares = 0

    #getting min number of posts to get average
    if len(user['aweme_list']) < 6:
        length = len(user['aweme_list'])
    else:
        length = 6
    
    #trim schema to take up less data
    for post in user['aweme_list']:
        timestamp = post['create_time']
        dt_object = datetime.fromtimestamp(timestamp)
        aweme_list.append({
        'author':
        {'region':post['author']['region'],
        'sec_uid':post['author']['sec_uid'],
        'unique_id':post['author']['unique_id'],
        'uid':post['author']['uid']},

        'music':
        {'title':post['music']['title']},

        'statistics':
        post['statistics'],

        'general':
        {'aweme_id':post['aweme_id'],
        'commerce_info':post['commerce_info'],
        'desc':post['desc'],
        'region':post['region'],
        'video_text':post['video_text'],
        'with_promotional_music':post['with_promotional_music'],
        'date':dt_object,
        'share_url':post['share_url']}
        })
        descSuperString+=post['desc']
        if (counter <(length+3)) and (counter > 3):
            totalComments += post['statistics']['comment_count']
            totalLikes += post['statistics']['digg_count']
            totalViews += post['statistics']['play_count']
            totalShares += post['statistics']['share_count']

    


        


        counter+=1

    #calculating averages
    averageComments = round(totalComments/length)
    averageLikes = round(totalLikes/length)
    averageViews = round(totalViews/length)
    averageShares = round(totalShares/length)
    

    #creating dictionaries to later add to the db
    userPosts = {'aweme_list':
    aweme_list,
    'cursors':
    {'max_cursor':user['max_cursor'],
    'min_cursor':user['min_cursor']}}

    #creating dictionary of averages and superString
    averages = {
    'views':averageViews,
    'likes':averageLikes,
    'shares':averageShares,
    'comments':averageComments,
    'superString':descSuperString,
    }
    #adding to db
    updateDate = date.strftime("%Y-%m-%d %H:%M:%S")
    print(updateDate)
    db.TokFl.find_one_and_update({'TikTok.user.sec_uid': userPosts["aweme_list"][0]["author"]["sec_uid"]}, {"$set":{"TikTok.userPosts":userPosts, 'TikTok.averages':averages, "TikTok.lastPostUpdate":str(updateDate)}})

    return userPosts["aweme_list"][0]["author"]["unique_id"]