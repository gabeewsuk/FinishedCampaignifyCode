from pymongo import MongoClient
import pymongo
import sys, os
import time

from Folder.db.dbConnect import connect
from Folder.routes.getUser import scrapeUsers
from Folder.routes.getUserId import getUserId
from Folder.parentFunctions.AddNewUsers.bulkWrite import addNewUsers
from Folder.parentFunctions.AddNewUsers.addUserPosts import newUsers_addUserPosts

def addNewUsersByUName(userNames):
    #need a function here that gets the userNames sends them to tokfluence to get the sec_uid
    user_ids = getUserId(userNames)
    addNewUsers(user_ids)
    newUsers_addUserPosts(user_ids)
    print("added new users")
    return "success"
    #need a function that takes the list of sec_uids then sends them in to scrape the user profiles

    


