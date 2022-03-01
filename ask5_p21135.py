print("Write Some Text In Order To Get The Following: ")
print("10 Most Used Words")
print("3 Most Used First Two-Letter Combos From Words")
print("3 Most Used First Three-Letter Combos From Words")
while True:
  sampleText = input()
  def convertToLoWh(sample):
    i = 0
    toReset = 0
    charList = list(sample)
    #sloppy way to fix index out of range
    asciiDump = [None]*(len(charList))
    while i < len(charList):
     asciiDump[i] = ord(charList[i])
     if i == (len(charList) - 1): toReset = 1
     i += 1
    #reset index without changing function
    if toReset == 1: i = 0
    while i < len(charList):
     if not charList[i].islower():
      if asciiDump[i] >= 65 and asciiDump[i] <= 90:
        asciiDump[i] += 32
      else:
        asciiDump[i] = 32
     if i == (len(charList) - 1): toReset = 1  
     i += 1
    if toReset == 1: i = 0 
    while i < len(charList):
      charList[i] = chr(asciiDump[i])
      i += 1
    parString = "".join(charList)
    return parString


  convPar = convertToLoWh(sampleText)
  #print(convPar)
  #convert to word list
  wordList = convPar.split()
  #print(wordList)
  
  def sizedlist(list, length):
    sizedList = [-1]*len(list)
    temp = [-1]*len(list)
    remCount = 0
    if (length == -1): 
      return list
    else:
      for u in range(len(list)):
        temp = list[u]
        #print(temp,"TEMPORARY LIST FOR SIZING")
        if len(temp) < length: 
          sizedList[u] = 0
        else: sizedList[u] = temp[:length]
      u = 0
      while u < (len(list) - remCount):
        if sizedList[u] == 0: 
            sizedList.pop(u)
            remCount += 1
            u = 0
        else: u += 1    
      #print(sizedList, "sizedList") 
      return sizedList  
      
  def blacklist(list, length,index):
    tempList = [-1]*10
    tempList = sizedlist(list,length)
    #print(tempList)
    indexList = []
    tempWord = tempList[index]
    for j in range(len(tempList)):
      if tempWord == tempList[j]: indexList.append(j)
    return indexList    
   
  
  def maxOf(list,length,howMany):
    tempList = [""]*10
    tempList = sizedlist(list, length)
    maxList = []
    timesFound = [1]*len(tempList)
    popCount = 0
    k = 0
    while k < (len(tempList) - popCount):
      tempWord = tempList[k]
      blackList = blacklist(list, length,k)
      if k != blackList[0]:
        timesFound[k] = 0
        tempList[k] = "0"
        timesFound[blackList[0]] += 1
      else:  
        timesFound[k] = tempList.count(tempWord)
      k += 1    
    popCount = 0
    u = 0
    while u < (len(tempList) - popCount):
      if timesFound[u] == 0: 
        timesFound.pop(u)
        tempList.pop(u)
        popCount += 1
        u = 0
      else: u += 1
    mergedList = zip(timesFound,tempList)    
    sortedList = [-1]*len(tempList)
    sortedList = sorted(mergedList,reverse = True)
    popCount = 0
    u = 0
    while u < (len(tempList) - popCount):
      if sortedList[u] == (0,'0'): 
        sortedList.pop(u)
        popCount += 1
        u = 0
      else: u += 1
    #print(sortedList,"THIS IS SORTED LIST", length)
    trimmedList = sortedList[:howMany]
    maxList = trimmedList
    return maxList
  
  topTen = maxOf(wordList,-1,10)
  twoFirst = maxOf(wordList,2,3)
  threeFirst = maxOf(wordList,3,3)
  print(f"10 Most Used Words:")
  print(topTen)
  print(f"2 Most Used Two-Letter Combos:")
  print(twoFirst)
  print(f"3 Most Used Three-Letter Combos:")
  print(threeFirst)
