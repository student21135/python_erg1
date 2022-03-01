import requests
import json
import math
urlContent = (requests.get('https://drand.cloudflare.com/public/latest')).text
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'}
latestDict = json.loads(urlContent) 
latestRand = latestDict["randomness"]

def stringPortion(step,list):
    finalList = [""]*(len(list)//step)
    for j in range(len(list)//step):
        for i in range(step):
            #print(j,i)
            finalList[j] += list[i+(j*step)]
    return finalList    

def hexToKINO(value):
    toInt = int(value,16)
    #print(toInt)
    toMod = (toInt % 80)
    #print(toMod)
    return toMod

splitList = stringPortion(2,latestRand) 
#print(splitList,latestRand)
finalList = [0]*32

for i in range(32):
    finalList[i] = hexToKINO(splitList[i])
temp = dict.fromkeys(finalList)
finalList = list(temp)
finalList.sort()
#print(finalList)

kinoContent = (requests.get('https://api.opap.gr/draws/v3.0/1100/last-result-and-active')).text
kinoDict = json.loads(kinoContent)
#kinoWin = json.loads(kinoDict["winningNumbers"])
#kinoNumbers = kinoDict["list"]
kinoNumbers = kinoDict['last']['winningNumbers']['list']
#print(len(finalList))
kinoNumbers.sort()
def equivComp(aList,bList):
    rightList = []
    equalCount = 0
    u = 0
    if len(aList) > len(bList):
        u = len(bList)
    else:
        u = len(aList)
    i = 0
    while i < u:
        found = False
        for j in range(u):
            if aList[i] == bList[j]:
                rightList.append(aList[i])
                found = True
        if found == True:
            equalCount += 1
        i += 1    
    return [equalCount,rightList]

sameAsKino = equivComp(finalList,kinoNumbers)
print('OUT OF 32 NUMBERS YOU WOULD HAVE GOT ',sameAsKino[0],' RIGHT')
print(sameAsKino[1])


