import requests
from decouple import config

def load_url(querystring):
    url = config("API_URL")+"/user-posts"
    headers = {
    'x-rapidapi-host': config("API_HOST"),
    'x-rapidapi-key': config("API_KEY")
   
    }

    #print(headers)
    #print(querystring)
    #print(url)
    response = requests.request("GET", url, headers=headers, params=querystring)
    while response.status_code == 429:
        print("API server is getting too many requests")
        time.sleep(10)
        response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()






   

test = load_url({"sec_user_id":"MS4wLjABAAAAw_nfZCqSdeYvqhe59GgwBFDFAyBLeI8Bo8rzmbkCZxSFQrdHTN5bTzOkv42egzvs","count":"32","max_cursor":"0"})
print(len(test["aweme_list"]))

#url = "https://scraptik.p.rapidapi.com/user-posts"

#querystring = {"sec_user_id":"MS4wLjABAAAAthIodSIVeKzQ3-xWFNydjPUL33PbaG6yVvnMXGpxB883-rZIkN63C0jww3X1K07x","count":"10","max_cursor":"0"}

#headers = {
 #   'x-rapidapi-host': "scraptik.p.rapidapi.com",
#    'x-rapidapi-key': "337fecf7d0msh62f6157b1c9669ap1fcbf2jsn748a8a0b6a62"
 #   }

#response = requests.request("GET", url, headers=headers, params=querystring)

#print(response.text)


#url = "https://scraptik.p.rapidapi.com/user-posts"

#{"sec_user_id":"MS4wLjABAAAAthIodSIVeKzQ3-xWFNydjPUL33PbaG6yVvnMXGpxB883-rZIkN63C0jww3X1K07x","count":"10","max_cursor":"0"}
#{'sec_user_id':'MS4wLjABAAAAthIodSIVeKzQ3-xWFNydjPUL33PbaG6yVvnMXGpxB883-rZIkN63C0jww3X1K07x','count':'100','max_cursor':'0'}

#headers = {
 #   'x-rapidapi-host': "scraptik.p.rapidapi.com",
 #   'x-rapidapi-key': "337fecf7d0msh62f6157b1c9669ap1fcbf2jsn748a8a0b6a62"
  #  }

#response = requests.request("GET", url, headers=headers, params=querystring)

#print(response.text)