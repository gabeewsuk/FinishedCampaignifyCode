from Folder.parentFunctions.Updates.UpdateDBSingleUser import updateSelectUsers
from Folder.db.Finders.dbFindSecUidByUname import findSecUidByUname

def readRoster():
  with open('Roster.csv', 'r') as f:
    file = csv.reader(f)
    my_list = list(file)
  print(my_list)
  return my_list
def updateByCsv(roster):  
    sec_uids = findSecUidByUname(roster)
    print(len(sec_uids))
    updateSelectUsers(sec_uids)
    print("done updating list from Roster.csv...")