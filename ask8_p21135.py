import random

#create board with custom choices of x,y
def customBoard(x,y):
  board = [[" " for j in range(y)] for i in range(x)]
  i = 0
  j = 0
  while i < x:
      while j < y:
          board[i][j] = "■"
          j += 2
      i += 1
      j = (i % 2) 
  i = 0
  #for i in range(x):
      #print(board[i])
  return board

#eightEight = customBoard(8,8)
#sevenEight = customBoard(7,8)
#eightSeven = customBoard(8,7)


#place tower and officer in random places
def initPieces(x,y):
    board = customBoard(x,y)
    posTowerX = random.choice(range(x))
    posTowerY = random.choice(range(y))
    posOfficerX = random.choice(range(x))
    posOfficerY = random.choice(range(y))
    while posTowerX == posOfficerX and posTowerY == posOfficerY:
        posOfficerX = random.choice(range(x))
        posOfficerY = random.choice(range(y))
    #posTower = [posTowerX,posTowerY]
    #posOfficer = [posOfficerX,posOfficerY]
    #print(posTower,"POSITION OF TOWER")
    #print(posOfficer, "POSITION OF OFFICER")
    #ebala antitheta xrwmata ypothetontas oti o kosmos genika douleuei se dark mode
    board[posTowerX][posTowerY] = "♜"
    board[posOfficerX][posOfficerY] = "♗"
    positions = [posTowerX,posTowerY,posOfficerX,posOfficerY]
    #for visual representation enable the two lines below
    #print("[---]"*y)
    #for i in range(x):
    #    print(board[i])
    #print("[---]"*y)    
    return positions

def scoringSystem(x,y):
    board = customBoard(x,y)
    posFetch = initPieces(x,y)
    posTower = [posFetch[0],posFetch[1]]
    posOfficer = [posFetch[2],posFetch[3]]
    tAdd = False
    oAdd = False
    winner = ""
    if posTower[0] == posOfficer[0] or posTower[1] == posOfficer[1]:
        tAdd = True
        winner = "TOWER WON THE GAME"
    elif abs(posFetch[0] - posFetch[2]) == abs(posFetch[1] - posFetch[3]):
        oAdd = True
        winner = "OFFICER WON THE GAME"
    score = [tAdd,oAdd]
    #to keep track of games remove hashtag from below and from line 69(nice)
    #if tAdd != oAdd: print(winner)
    return score

def runGame(x,y,rep):
    towScore = 0
    offScore = 0
    for i in range(rep):
        #print("ROUND ",i," :")
        roundWinner = scoringSystem(x,y)
        if roundWinner[0] == True:
            towScore += 1
        elif roundWinner[1] == True:
            offScore += 1
    print("OUT OF ",rep," GAMES TOWER WON ",towScore," GAMES AND OFFICER WON ",offScore)
    print("BOARD SIZE",x,"x",y)

exec(runGame(8,8,100),runGame(7,8,100),runGame(7,7,100))

#perissotera disabled lines einai apla diagnostic kai kala na checkarw an douleuei o algorithmos swsta
