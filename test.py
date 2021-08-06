import requests
from decouple import config
from Folder.db.dbConnect import connect
import pymongo



from Folder.db.Finders.dbFindAweme_List import findAweme_List
from Folder.db.Averages.AveragesCalc import averageCalc


#updateAverages()

db = connect('TikScrape')

db.TokFl.delete_many({})

