def searchMatch(worldid): #search the Match your World is participating in with the world id
    n = 0
    j = 0
    suffix = "wvw/matches/"
    allmatches = getMatches()
    for i in allmatches:
        currentmatch = allmatches[n]
        participants = requests.get(api_base + suffix + currentmatch)
        participants = participants.json()
        worldids_temp = participants["all_worlds"]
        red = worldids_temp["red"]
        green = worldids_temp["green"]
        blue = worldids_temp["blue"]
        for i in red:
            if(int(red[j]) == worldid):
                #print(currentmatch) #debug
                return currentmatch
            j += 1
        j = 0
        for i in green:
            if(int(green[j]) == worldid):
                #print(currentmatch) #debug
                return currentmatch
            j += 1
        j = 0
        for i in blue:
            if(int(blue[j]) == worldid):
                #print(currentmatch) #debug
                return currentmatch
            j += 1
        j = 0
        n += 1
    return 1
