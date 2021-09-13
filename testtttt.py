querystrings = [{'username': "{'username': '2151994476'}"}, {'username': "{'username': 'tamaraaanthonyy'}"}, {'username': "{'username': 'bheemagurjar01'}"}, {'username': "{'username': 'sandaleony'}"}, {'username': "{'username': 'richnana10'}"}, {'username': "{'username': 'drarry_fan_2uwu'}"}, {'username': "{'username': 'poojamalhotr'}"}, {'username': "{'username': 'cumacera'}"}, {'username': "{'username': 'tsew_tk'}"}, {'username': "{'username': 'vaneroldanb'}"}, {'username': "{'username': 'scottiethompson06'}"}, {'username': "{'username': 'sidhu_moosewala.pakistan'}"}, {'username': "{'username': 'karinakliauz'}"}]

for querystring in querystrings:
    #print(querystring)
    new = querystring["username"]
    new = new.replace("{'username': '", "")
    new = new.replace("'}", "")
    #print("querystring is:")
    print(new)
