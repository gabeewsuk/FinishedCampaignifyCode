from pymongo import MongoClient
import pymongo
import sys, os
import time

from Folder.db.dbConnect import connect
from Folder.routes.getUser import scrapeUsers
from Folder.routes.getUserId import getUserId
from Folder.parentFunctions.AddNewUsers.bulkWrite import addNewUsers
from Folder.parentFunctions.AddNewUsers.addUserPosts import newUsers_addUserPosts

#add new users by an array of usernames
def addNewUsersByUName(userNames):
    #gets user id for each user in array
    sec_uids = getUserId(userNames)
    #adds users in to db
    print(sec_uids)
    print("SEC USER IDS^")
    print(len(sec_uids))
    addNewUsers(sec_uids)
    #adds posts to all users
    newUsers_addUserPosts(sec_uids)
    print("added new users by username Array...")

    


