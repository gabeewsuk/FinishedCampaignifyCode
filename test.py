import requests
from decouple import config

from Averages.AverageViews import averageViews
from Averages.AverageLikes import averageLikes
from Averages.AverageShares import averageShares
from Averages.AverageComments import averageComments


#views = averageViews()
#print(views)

#likes = averageLikes()
#print(likes)

#comments = averageComments()
#print(comments)

shares = averageShares()
print(shares)