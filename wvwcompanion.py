import gw2lib
import json

f = open("api_key.txt", "r")
key = f.read()
f.close


def printMatchInfo(matchid): #print some basic match info for given matchid
    n = 0
    green = []
    red = []
    blue = []
    matchinfo = gw2lib.getAllMatchInfo(matchid)
    participants = matchinfo["all_worlds"] 
    greenids = participants["green"] 
    redids = participants["red"]
    blueids = participants["blue"]
    print("start date: " + matchinfo["start_time"])
    print("end date: " + matchinfo["end_time"])
    for i in greenids:
        green.append(gw2lib.getWorldname(greenids[n]))
        n += 1
    n = 0
    for i in redids:
        red.append(gw2lib.getWorldname(redids[n]))
        n += 1
    n = 0
    for i in blueids:
        blue.append(gw2lib.getWorldname(blueids[n]))
        n += 1
    n = 0
    gkills = gw2lib.getKills(matchinfo, "green")
    gdeaths = gw2lib.getDeaths(matchinfo, "green")
    gkd = gkills/gdeaths #green K/D
    rkills = gw2lib.getKills(matchinfo, "red")
    rdeaths = gw2lib.getDeaths(matchinfo, "red")
    rkd = rkills/rdeaths #red K/D
    bkills = gw2lib.getKills(matchinfo, "blue")
    bdeaths = gw2lib.getDeaths(matchinfo, "blue")
    bkd = bkills/bdeaths #blue K/D
    print()
    print("green Team: ", end = "")
    print(*green, sep = ", ")
    #print(greenids) #debug
    print("Kills: " + str(gkills))
    print("Deaths: " + str(gdeaths))
    print("K/D: " + str(gkd))
    print()
    print("red Team: ", end = "")
    print(*red, sep = ", ")
    #print(redids) #debug
    print("Kills: " + str(rkills))
    print("Deaths: " + str(rdeaths))
    print("K/D: " + str(rkd))
    print()
    print("blue Team: ", end = "")
    print(*blue, sep = ", ")
    #print(blueids) #debug
    print("Kills: " + str(bkills))
    print("Deaths: " + str(bdeaths))
    print("K/D: " + str(bkd))
    print()
    return

def listWorlds():
    worlds = gw2lib.getAllWorlds()
    worlds = sorted(worlds)
    for i in range(len(worlds)):
        print(str(worlds[i][0]) + " ID: " + str(worlds[i][1]))
    return
   
#printMatchInfo(gw2lib.getMatchId(gw2lib.getAccountWorld(key)))
gw2lib.getMaterials(key)