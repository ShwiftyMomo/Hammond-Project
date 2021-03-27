import random

#In this fileI write several strategies

def min_I_Strategy(body):  #chooses first available space
    for i in range(len(body)):
        for j in range(len(body[i])):
            if body[i][j] == 0:
                return [i,j]
    print("no valid move found")

def HammondStrategy(body,numSamples = 100):     #implements Hammmond's strategy
    size = len(body)
    tempBoard = Board(size)
    tempBoardbody = Board(size,body)

    blankIndices = []
    for i in range(size):
        for j in range(i+1):
            if body[i][j] == 0:
                blankIndices += [[i,j]] #finds black points


    tempBoard2 = Board(size)
    for i in range(size):
        for j in range(i+1):
            tempBoard2.body[i][j] = body[i][j]

    for i in range(numSamples):
        for pair in blankIndices:
            tempBoard2.body[pair[0]][pair[1]] = random.choice([-1,1]) #randomizes blank points

        path = tempBoard2.findBestPath()[0][1] #optimal path

        y = 0
        for j in range(size-1):
            tempBoard.body[j][y] +=1
            if path[j] == 1:
                y += 1
        tempBoard.body[size-1][y] +=1

    retInd = [0,0]
    maxHits = 0
    for i in range(size):  #counts the point with the most hits
        for j in range(i+1):
            if body[i][j] == 0 and tempBoard.body[i][j] > maxHits:
                retInd = [i,j]
                maxHits = tempBoard.body[i][j]
    return retInd

def OptimalStrategy(body): #Warning: will take long time to run, for boards of size greater than or equal to 4, probably will not be able to finish
    #will be defined recursively
    def Expected(choice): #calculates the Expected score of a choice with perfect strategy
