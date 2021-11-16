import csv
from blaster import blasterFunc
from textToCSV import updateTagScreenShot
from textToCSV import readFile
from addTag import updateTag
from csvToArray import readRoster
from QueryDB import QueryData
from Folder.parentFunctions.AddNewUsers.newUser_addUserByName import addNewUsersByUName
import datetime
from Folder.db.dbConnect import connect
from QueryDB import toDF
from updateUsersByCsv import updateByCsv
from z import addEmailBio

from y import findTags

#HERE IS WHERE YOU MAKE THE EDITS
def blastMessage():
    Meat = []
    with open("names.csv", mode='r', encoding='utf-8-sig') as f:
        records = csv.DictReader(f)
        for row in records:
            Meat.append(row)

    print(Meat)
    userName = "lgbt.50"
    passWord = "SpartanTeam47@!"
    credentials = Meat
    message = "You can easily make {price}+ with this opportunity!"
    message2 = "Hey {name}! We are putting together a creator network to share promotions so that you can easily increase your revenue. All you would have to do is simply put us in contact with some of the brands that you’ve worked with in the past and if we end up working with them, we’ll compensate you with 10 percent of the revenue we make from that campaign. (We typically work with 5-10 creators per campaign so it could be very lucrative for you!)"
    message3 = "Would you be interested in joining our creator promotions network? We would also include you in the network and will bring you deals that we get from creators similar to you!"
    message4 = "Let me know if you are interested, this opportunity only stands for the next few days!"
    blasterFunc(userName, passWord, credentials, message, message2, message3, message4)


#This section is used for Querying returns output.csv
#QueryDataAny()

#HERE IS WHERE YOU MAKE THE EDITS
def QueryDataAny():
  db = connect("TikScrape")
  #This is where you set the date for have posted atleast once since this date
  date_time_str = '2021-11-1'
  date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d')

  cursor = db.TokFl.find(
    {
    
        "$or": [

          {"instaBioEmail":{"$exists":True}},
          {"tiktokBioEmail":{"$exists":True}},


          #{ "Instagram.user.bio": { "$regex": "@", "$options": "i" }},
            #{"Instagram.user.follower_count":{"$gt":20000}},
            #{"Tag":{"$in":Tag}},

          
          #{ "TikTok.user.signature": { "$regex": "", "$options": "i" }},
        
          #{ "TikTok.averages.superString": { "$regex": "#sponsored", "$options": "i" }},
          #{ "TikTok.user.signature": { "$regex": "", "$options": "i" }},
          #{ "TikTok.user.signature": { "$regex": "🌈", "$options": "i" }},
          #{ "TikTok.user.signature": { "$regex": "👨‍❤️‍👨", "$options": "i" }}
          #{"TikTok.userPosts.aweme_list.0.general.date":{ "$gt": date_time_obj}},
          #{"TikTok.user.":{ "$exists":False }},
           #{"TikTok.lastPostUpdate":{ "$gt": "2021-11-13 22:50:09"}},
            #{"TikTok.userPosts.aweme_list.2.general.date":{ "$gt": date_time_obj}},
          #{"TikTok.userPosts.aweme_list.3.general.date":{ "$gt": date_time_obj}},
           # {"TikTok.userPosts.aweme_list.4.general.date":{ "$gt": date_time_obj}},
        ],
        "$and": [
              #{ "Instagram.user.bio": { "$regex": ".com", "$options": "i" }},

           #{"TikTok.userPosts.aweme_list.2.general.date":{ "$gt": date_time_obj}},
         # {"TikTok.userPosts.aweme_list.3.general.date":{ "$gt": date_time_obj}},
            #{"TikTok.userPosts.aweme_list.4.general.date":{ "$gt": date_time_obj}},
        #{ "TikTok.user.signature" : { "$regex": {'$nin': [
        #'@gmail.com']},
        #{ "Instagram.user.bio" : { "$regex": {'$nin': [
        #'@gmail.com']}
          { "Instagram.user.bio": { "$regex": "", "$options": "i" }},
        # { "Instagram.user.bio": { "$regex": "@gmail.com", "$options": "i" }},
       # {"$or": [
         # {"$nin":[
          #{ "Instagram.user.bio": { "$regex": ".com", "$options": "i" }},
          #{ "Instagram.user.bio": { "$regex": "@", "$options": "i" }},
                    #{ "Instagram.user.bio": { "$regex": "", "$options": "i" }},


          #{ "TikTok.user.signature": { "$regex": "@", "$options": "i" }},
           #{ "TikTok.user.signature": { "$regex": ".com", "$options": "i" }},

        #]}
        #]}
          #{"TikTok.userPosts.aweme_list.0.general.desc":{ "$regex": "#fyp", "$options": "i" }},
          #"$or":[
            #{"TikTok.userPosts.aweme_list.0.general.date":{ "$gt": date_time_obj}},
          # {"TikTok.userPosts.aweme_list.1.general.date":{ "$gt": date_time_obj}},
          # {"TikTok.userPosts.aweme_list.2.general.date":{ "$gt": date_time_obj}},
          # {"TikTok.userPosts.aweme_list.3.general.date":{ "$lt": date_time_obj}},
          #  {"TikTok.userPosts.aweme_list.4.general.date":{ "$gt": date_time_obj}},
          #"$gt":"2021-10-10T19:51:48.000+00:00"ç

            #{ "TikTok.user.signature": { "$regex": "", "$options": "i" }},

        #{"TikTok.lastPostUpdate": {"$gt":"2021-09-27 02:58:56"}}
          #{ "TikTok.user.signature": { "$regex": ".com", "$options": "i" }},
          #{ "TikTok.averages.views": { "$gt": 75000, "$lt":25000000000}},
          #{"Instagram.user.follower_count":{"$lt":10000}},#,"$lt":1000000000000000}} ,
        # {"TikTok.userPosts.aweme_list.author.region": { "$regex": "US", "$options": "i" }}
          
        ],

      }
      )
      
      

  x= 0
  data = []
  sec_uids = []
  z = 0
  for document in cursor:
    z+=1
    try:
      print(document["tiktokBioEmail"])
      print(document["instaBioEmail"])
      instaLink = "https://www.instagram.com/"+str(document["TikTok"]["user"]["ins_id"])
      TTLink = "https://www.tiktok.com/@"+str(document["TikTok"]["user"]["unique_id"])+"?"

      f = [document["TikTok"]["user"]["ins_id"], document["TikTok"]["user"]["unique_id"],
      document["Instagram"]["user"]["follower_count"], 
      document["TikTok"]["averages"]["views"], document["TikTok"]["averages"]["likes"], document["TikTok"]["averages"]["comments"],
      document["TikTok"]["user"]["follower_count"], instaLink, TTLink, document["TikTok"]["user"]["nickname"], document["tiktokBioEmail"], document["instaBioEmail"]
      ]
      data.append(f)
      x+=1
     
    except Exception as e:
      try:
        instaLink = "https://www.instagram.com/"+str(document["TikTok"]["user"]["ins_id"])
        TTLink = "https://www.tiktok.com/@"+str(document["TikTok"]["user"]["unique_id"])+"?"

        f = [document["TikTok"]["user"]["ins_id"], document["TikTok"]["user"]["unique_id"],
        document["Instagram"]["user"]["follower_count"], 
        document["TikTok"]["averages"]["views"], document["TikTok"]["averages"]["likes"], document["TikTok"]["averages"]["comments"],
        document["TikTok"]["user"]["follower_count"], instaLink, TTLink, document["TikTok"]["user"]["nickname"], document["tiktokBioEmail"], document["instaBioEmail"]
        ]
        data.append(f)
        x+=1
      except:
        try:
          instaLink = "https://www.instagram.com/"+str(document["TikTok"]["user"]["ins_id"])
          TTLink = "https://www.tiktok.com/@"+str(document["TikTok"]["user"]["unique_id"])+"?"

          f = [document["TikTok"]["user"]["ins_id"], document["TikTok"]["user"]["unique_id"],
          document["Instagram"]["user"]["follower_count"], 
          document["TikTok"]["averages"]["views"], document["TikTok"]["averages"]["likes"], document["TikTok"]["averages"]["comments"],
          document["TikTok"]["user"]["follower_count"], instaLink, TTLink, document["TikTok"]["user"]["nickname"], "NA", document["instaBioEmail"]
          ]
          data.append(f)
          x+=1
        except:
          try:
            
            instaLink = "https://www.instagram.com/"+str(document["TikTok"]["user"]["ins_id"])
            TTLink = "https://www.tiktok.com/@"+str(document["TikTok"]["user"]["unique_id"])+"?"

            f = [document["TikTok"]["user"]["ins_id"], document["TikTok"]["user"]["unique_id"],
            document["Instagram"]["user"]["follower_count"], 
            document["TikTok"]["averages"]["views"], document["TikTok"]["averages"]["likes"], document["TikTok"]["averages"]["comments"],
            document["TikTok"]["user"]["follower_count"], instaLink, TTLink, document["TikTok"]["user"]["nickname"], document["tiktokBioEmail"], "NA"
            ]
            data.append(f)
            x+=1
          except:
            try:
                instaLink = "https://www.instagram.com/"+str(document["TikTok"]["user"]["ins_id"])
                TTLink = "https://www.tiktok.com/@"+str(document["TikTok"]["user"]["unique_id"])+"?"

                f = [document["TikTok"]["user"]["ins_id"], document["TikTok"]["user"]["unique_id"],
                "NA", 
                document["TikTok"]["averages"]["views"], document["TikTok"]["averages"]["likes"], document["TikTok"]["averages"]["comments"],
                document["TikTok"]["user"]["follower_count"], instaLink, TTLink, document["TikTok"]["user"]["nickname"], document["tiktokBioEmail"], "NA"
                ]
                data.append(f)
                x+=1
            except:
              try:
                instaLink = "https://www.instagram.com/"+str(document["TikTok"]["user"]["ins_id"])
                TTLink = "https://www.tiktok.com/@"+str(document["TikTok"]["user"]["unique_id"])+"?"

                f = [document["TikTok"]["user"]["ins_id"], document["TikTok"]["user"]["unique_id"],
                "NA", 
                document["TikTok"]["averages"]["views"], document["TikTok"]["averages"]["likes"], document["TikTok"]["averages"]["comments"],
                document["TikTok"]["user"]["follower_count"], instaLink, TTLink, document["TikTok"]["user"]["nickname"],  "NA", "NA"
                ]
                data.append(f)
                x+=1
              except:
                print("no instagram")
  toDF(data)
  print(z)
  print(x)








#this section is for screenshots to database with a tag! DON'T TOUCH
def ScreenShotToDB(Tag):
    newArr = readFile()
    addNewUsersByUName(newArr)
    updateTagScreenShot(newArr, Tag)
    addEmailBio(Tag)
    QueryData(Tag)


def CSVToDB(Tag):
    Roster = readRoster()
    addNewUsersByUName(Roster)
    updateTagScreenShot(Roster, Tag)
    addEmailBio(Tag)
    QueryData(Tag)



#This section is for using a csv to add tags! DON'T TOUCH
def TagByCSV(Tag):
    Roster = readRoster()
    updateTag(Tag)
    addEmailBio(Tag)
    QueryData(Tag)
    
def updateDataByCSV(Tag):
  roster = readRoster()
  updateByCsv(roster)
  updateTag(Tag)
  addEmailBio(Tag)
  QueryData(Tag)
    


#---------------------------------------------------------------
if __name__ == "__main__":
    #this section is for screenshots to database with a tag! 
    #Takes file.txt returns output.txt
    #You must define the Tag in the line below
    #--
    #Tag = "XTESTNOV11"
    #ScreenShotToDB(Tag)
    #--

    #This section is for using a csv to add tags. 
    #Takes Roster.csv, returns output.csv
    #You must define the Tag in the line below
    #--
    #Tag = "JOSEANDXTEST"
    #TagByCSV(Tag)
    #--

    #This Section is for sending out blast messages! 
    #Takes names.csv
    #Go to Line 16 to make edits to change message
    #--
    #blastMessage()
    #--

    #This section is used for Querying returns output.csv 
    #You need to edit the function above to query specific results starts on line 34
    #--
    #QueryDataAny()
    #--

    #this seciotn is used for adding to the database by csv
    #you takes Roster.csv and returns output.csv
    #choose a Tag
    #--
    #Tag = ""
    #CSVToDB(Tag)
    #--

    #this section is used for updating users data by csv... THESE USERS MUST ALREADY BE IN THE DATABASE
    #This takes Roster.csv and returns output.csv
    #--
    #Tag = ""
    #updateDataByCSV(Tag)
    #--

    #this section is used for querying users based on a Tag
    #This returns output.csv
    #Tag="Roster"
    #QueryData(Tag)

    tags = findTags()
    print(tags)



