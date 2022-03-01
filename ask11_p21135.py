import requests
import json
import math
urlContent = (requests.get('https://drand.cloudflare.com/public/latest')).text
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'}
latestDict = json.loads(urlContent) 
latestRound = latestDict["round"]
template = 'https://drand.cloudflare.com/public/'
print("LATEST ROUND IS ",latestRound)
def fetchRand(length,latest):
    valueList = [0]*length
    for i in range(length):
        tempUrl = str(template + str(latest - i))
        tempFetch = (requests.get(tempUrl)).text
        tempDict = json.loads(tempFetch)
        valueList[i] = tempDict["randomness"]
        #print('VALUE OF RANDOMNESS FROM ROUND ',(latest - i))
        #print(valueList[i])
    return valueList

#exec(fetchRand(20,latestRound))   
    
def toHexSum(length):
    tempValues = []*length
    tempValues = fetchRand(length,latestRound)
    textSum = ""
    for i in range(length):
        textSum += str(tempValues[i])
    toInt = int(textSum,16)
    hexSum = hex(toInt)
    print("YOUR VALUES ARE ",hexSum)
    return hexSum
    
hexChar = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
for i in range(16):
    hexChar[i] = int(hexChar[i],16)
    hexChar[i] = hex(hexChar[i])

def probCalc(content,charlist):
    valueFreq = [0]*len(charlist)
    probList = [0]*len(charlist)
    strDump = [""]*len(charlist)
    for i in range(len(charlist)):
        strDump[i] = str(charlist[i])
        valueFreq[i] = strDump.count(charlist[i])
        probList[i] = valueFreq[i]/(len(content))
        #print(probList[i])
    return probList

def entropyOf(content,states,charlist):
    entropy = 0
    tempSum = 0
    probFetch = []*len(charlist)
    probFetch = probCalc(content,charlist)
    for i in range(states):
        tempSum += probFetch[i]*math.log(probFetch[i],16)
    entropy = abs(tempSum)
    print("THE ENTROPY OF YOUR TEXT IS ",entropy)
    return entropy

c = toHexSum(20)    
exec(entropyOf(c,16,hexChar))        
