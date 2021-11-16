import pandas as pd
 

def toDF(data):
# initialize list of lists
    # Create the pandas DataFrame
    df = pd.DataFrame(data, columns = ['instagram', 'TikTok', 'ins_followers', 'aViews', 'aLikes', 'aComments', 'tikFollowers', "InstaLink",  "TikTokLink", "name"])
    
    # print dataframe.
    print(df)