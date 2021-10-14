import requests
import json

api_base = "https://api.guildwars2.com/v2/"

#before the Repo goes public remove all API-Keys in Comments and in commit history

def getMatches(): #just get all available matchid's
    suffix = "wvw/matches"
    matcheid = requests.get(api_base + suffix)
    matcheid = matcheid.json()
    return matcheid

def getWorldname(worldid): #get the clear name of a worldid 
    suffix = "worlds?ids=" + str(worldid)
    name = requests.get(api_base + suffix)
    name = name.json()
    name = name[0]
    name = name["name"]
    return name
    
def getMatchId(worldid): #give back the MatchId, needs the worldid
    suffix = "wvw/matches/overview?world="
    world = requests.get(api_base + suffix + str(worldid))
    world = world.json()
    matchid = world["id"]
    return matchid

def getAllMatchInfo(matchid): #drops all matchinfo when given the matchid
    suffix = "wvw/matches/"
    matchdetails = requests.get(api_base + suffix + str(matchid))
    matchdetails = matchdetails.json()
    return matchdetails

def getKills(match, team): #give back kills out of given match !object! not matchid, to avoide unnecessary requests; give it the output of getAllMatchInfo + team (red, blue, green)
    kills = match["kills"]
    kills = kills[team]
    return kills

def getDeaths(match, team): #give back deaths out of given match !object! not matchid, to avoide unnecessary requests; give it the output of getAllMatchInfo + team (red, blue, green)
    deaths = match["deaths"]
    deaths = deaths[team]
    return deaths

def getAllWorlds(): #give back an 2 dimensional array of all worlds where the second dimension is used for id/name [x][1] gives the id and [x][0] the name
    suffix = "worlds?ids=all"
    allworlds = requests.get(api_base + suffix)
    allworlds = allworlds.json()
    servercount = len(allworlds)
    worlds = [[0 for i in range(2)] for j in range(servercount)]
    for i in range(servercount):
        tempworld = allworlds[i]
        worlds[i][0] = tempworld["name"]
        worlds[i][1] = tempworld["id"]
    return worlds

def getAccountData(api_key): #get the unspecific account data example: https://api.guildwars2.com/v2/account?access_token=***REMOVED***
    suffix = "account?access_token="
    accdata = requests.get(api_base + suffix + api_key)
    accdata = accdata.json()
    return accdata

#TODO: directly give struct and not the key to minimize requests for all following functions that use the same struct

def getAccountWorld(api_key): #filter account data for WorldId (ServerId), needs API key
    accdata = getAccountData(api_key)
    worldid = accdata["world"]
    return worldid

def getFLevel(api_key): #filter account data for Fractal level, needs API key
    accdata = getAccountData(api_key)
    flevel = accdata["fractal_level"]
    return flevel

def getMaterials(api_key): #get Account Materials and put the name in the struct for every item (normal api call only gives item-ids back)
    suffix = "account/materials?access_token="
    materials = requests.get(api_base + suffix + api_key)
    materials = materials.json()
    for i in range(len(materials)):
        current_material = materials[i]
        itemid = current_material["id"]
        current_material["name"] = getItemName(itemid)
        materials[i] = current_material
        print(materials[i]) #debug
    return

def getItemInfo(itemid): #get whole struct of an item example: https://api.guildwars2.com/v2/items/82761
    suffix = "items/"
    item = requests.get(api_base + suffix + str(itemid))
    item = item.json()
    return item

def getItemName(itemid): #just get the name of an item when u go the id
    item = getItemInfo(itemid)
    item_name = item["name"]
    return item_name