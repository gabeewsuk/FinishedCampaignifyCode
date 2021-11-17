from Folder.db.dbConnect import connect
from datetime import datetime as d


#Finding user and updating with correct trimmed schema
def findAndUpdateUser(db, user):
    date = d.now()
    #check if user exitss
    if user["user"] == None:
        print("This no longer exists")

    else:
        #updating db if it does not exist
        try:
            db.TokFl.find_one_and_update({'TikTok.user.sec_uid': user["user"]["sec_uid"]},
            {"$set":
            {"TikTok.user.avatar_thumb":user["user"]["avatar_thumb"]["url_list"][0],
                #"TikTok.user.bio_url":user["user"]['bio_url'],
            "TikTok.user.follower_count":user["user"]['follower_count'],
            "TikTok.user.following_count":user["user"]['following_count'],
            "TikTok.user.ins_id":user["user"]['ins_id'],
            "TikTok.user.nickname":user["user"]['nickname'],
            "TikTok.user.signature":user["user"]['signature'],
            "TikTok.user.total_favorited":user["user"]['total_favorited'],
            "TikTok.user.twitter_id":user["user"]['twitter_id'],
            "TikTok.user.twitter_name":user["user"]['twitter_name'],
            "TikTok.user.uid":user["user"]['uid'],
            "TikTok.user.unique_id":user["user"]['unique_id'],
            "TikTok.user.youtube_channel_id":user["user"]['youtube_channel_id'],
            "TikTok.user.youtube_channel_title":user["user"]['youtube_channel_title'],
            #"TikTok.user.commerce_user_info.ad_experience_entry":user["user"]['commerce_user_info']['ad_experience_entry'],
            "TikTok.lastUserUpdate":date.strftime("%Y-%m-%d %H:%M:%S")}},upsert = True)
        except Exception as Exc:
            print("exceptions when updating user")
            print(Exc)
    return user["user"]["nickname"]
