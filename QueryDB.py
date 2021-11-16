from pymongo import MongoClient
import time
import pymongo
import pandas as pd
import datetime

from Folder.db.dbConnect import connect

def toDF(data):
    df = pd.DataFrame(data, columns = ['instagram', 'TikTok', 'ins_followers', 'aViews', 'aLikes', 'aComments', 'tikFollowers', "InstaLink",  "TikTokLink", "name", "Email1", "Email2"])
    
    df.to_csv('output.csv', index = False, header = True)





def QueryData(Tag):
  #find all SecUids in the db... Used for referencing scraping and updating
  print("Fining ids for users from db")
  db = connect("TikScrape")
  #This is where you set the date for have posted atleast once since this date
  date_time_str = '2021-10-8 08:15:27'
  date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')

  cursor = db.TokFl.find(
    {
    
       

    
            "Tag":{ "$regex": Tag, "$options": "i" }

          
          
        
          

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
