from pymongo import MongoClient
import time

from Folder.db.Finders.dbFindSecUid import findSecUid

#check mongo for duplicate records... currently not used for anything
def checkDuplicate(sec_uid):
    #pulls all sec_uid then checks to see if this one is in that list
    sec_uids = findSecUid()
    if sec_uid in sec_uids:
        exists = true
    else:
        exists = false
    return exists