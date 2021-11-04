from pymongo import MongoClient
import time
import pymongo
import pandas as pd
from datetime import datetime as d


from Folder.db.dbConnect import connect

def updateTag():
    date = d.now()

    x  = 0
    print("Fining ids for users from db")
    db = connect("TikScrape")
    #gets all users from the db list above^ and then only shows the sec_uid to reference user##
    Roster = ['minnieandtink', 'alexcortex', 'iamdavante', 'gurmyaujla', 'rrubee', 'cjtooicy', 'hannah.raisor48', 'iamislondy', 'ria_d3miri', 'shaihatten', 'aliciacastro___', 'bxbyymariii', 'mm6la', 'jade.a.roo', 'cecegangg', 'sybil.kappert', 'laurynandsteph', 'angxsav', 'alexis_santiago', 'caseyiscrazy', 'rebecca.g.young', 'hopealiviia', 'karinandskylerofficial', 'ellieeandlisa', 'lesliehannahbelle', 'camerongraggg', 'genlacombe', 'ilialeya', 'selabxby2.0', 'bon.bon.voyage', 'rothestudtv', 'the.lolodee', 'papifranqui', 'maggiegranttt', 'aubreytb14', 'artiethepixieee', 'theonlynoah_withnoark', '..alissa08', 'emiliemartian98', 'wgibbss', 'kyileeannelsten', 'okokveronica', 'selenagallow', '_ambereileen', 'itsjustnicole__', 'thatpunkwitch', 'izzy_stone098', 'alexa_and_maria_', 'devorelol', 'maggieannle', 'zoestoller', 'tyetun', 'athenalayna', 'himorg', 'paigedumars', 'kayleekawaii', 'theskyfieri', 'delaneybbrownn', 'soymaaleja', 'imaristuart', 'sierrakai.1', 'cici_cici_7', 'seanghedi', 'vanessafpena', 'alexispainterr', 'maihualee01']
    z = 0
    for x in Roster:
        print(x)
        try:
            #insTiktokFollowerRate = document['Instagram']['user']['follower_count']/document['TikTok']['user']['follower_count']
            db.TokFl.find_one_and_update({'TikTok.user.unique_id': x},
            {"$set":
            {
            #"specialStats.insToTikTokRatio": insTiktokFollowerRate,
            "Tag": "Roster",
            }},upsert = True)
            z+=1


            
 
        except Exception as e: 
            print(e)
            print("not working")

    print(z)

updateTag()
        
    
