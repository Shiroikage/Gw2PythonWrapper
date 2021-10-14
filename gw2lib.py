import requests
import json

api_base = "https://api.guildwars2.com/v2/"


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

def getAllMatchInfo(matchid): #drops all matchinfo when goven the matchid
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

def getAccountData(api_key): #get the unspecific account data
    suffix = "account?access_token="
    accdata = requests.get(api_base + suffix + api_key)
    accdata = accdata.json()
    return accdata

def getAccountWorld(apikey): #filter account data for WorldId (ServerId)
    accdata = getAccountData(apikey)
    worldid = accdata["world"]
    return worldid

