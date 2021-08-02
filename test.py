import requests
from decouple import config

from Folder.db.Averages.AverageShares import averageShares
from Folder.db.Averages.AverageComments import averageComments
from Folder.db.Averages.AverageViews import averageViews
from Folder.db.Averages.AverageLikes import averageLikes
from Folder.parentFunctions.Updates.UpdateDBAverages import updateAverages
from Folder.db.Finders.dbFindAweme_List import findAweme_List
from Folder.db.Averages.AveragesCalc import averageCalc


updateAverages()

