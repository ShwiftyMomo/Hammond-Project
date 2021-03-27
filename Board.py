from Player import Player
import random
import time

class Board:
    def __init__(self, size, body = None):
        self.size = size

        self.body = []

        self.numTurns = 0 #counts the number of turns that have taken place

        for i in range(size):
            self.body +=[[0 for j in range(i+1)]]

            #initializes body as all 0. The ith list will have i elements
            #If the list is printed, then the diagonal will go up right instead of down right
            #The last list is the longest and is the booundary of the board
            #0 is empty space, 1 is player 1, -1 is player 2

        if body != None: #checks that body is correct
            bodyCorrect = True
            if type(body) == list and len(body) == size:
                for i in range(size):
                    if type(body[i])==list and len(body[i])==i+1:
                        for j in range(i+1):
                            if body[i][j] not in [-1,0,1]:
                                bodyCorrect = False
                                print("error1")
                    else:
                        bodyCorrect = False
                        print("error2")
            else:
                bodyCorrect = False
                print("error3")

            if bodyCorrect:
                self.body = body
            else:
                print("body input was incorrect")

    def __str__(self):
        retString = ""
        for i in self.body:
            retString += str(i) + "\n"
        return retString

    def randomizeBoard(self):
        testBody = []
        for i in range(self.size):
            temp =[]
            for j in range(i+1):
                temp += [random.choice([-1,1])]
            testBody += [temp]
        self.body = testBody

    def isFilled(self): #checks if every entry has a -1 or 1, has a new value entered
        for i in range(self.size):
            for j in range(i+1):
                if self.body[i][j] == 0:
                    return False
        return True

    def findBestPath(self,i=0): #finds the best path from a particular location. Returns a list with the value and the path in it. 0 will indicate forward, and 1 is forward and up
        if not self.isFilled():
            print("The Board is not filled")
        else:
            if i == self.size - 1:               #function is recursively defined. This is the base case when the point is on the edge
                return [[self.body[i][j],[]] for j in range(i+1)] #creates all of the base paths
            else:
                recursivePath = self.findBestPath(i+1)
                retList = []
                for j in range(i+1):
                    choicePath1 = recursivePath[j] #the path just going forward 1, not up
                    choicePath2 = recursivePath[j+1]  #the path going forward and up

                    if choicePath1[0] > choicePath2[0]: #forward is the best path
                        retList += [[self.body[i][j] + choicePath1[0], [0] + choicePath1[1]]]

                    elif choicePath2[0] > choicePath1[0]: #forward and up is the best path
                        retList += [[self.body[i][j] + choicePath2[0], [1] + choicePath2[1]]]

                    else: #both paths are equal, for now will arbitrarily choose choicePath1
                        retList += [[self.body[i][j] + choicePath1[0], [0] + choicePath1[1]]]
                return retList

    def turn(self,player1,player2): #player will be a class
        if self.numTurns < self.size * (self.size + 1)/2:
            randnum = random.randint(0,2)
            if randnum == 0:
                move = player1.move(self.body) + [1] #move will be a 2 element list with the location that the player goes
            else:
                move = player2.move(self.body) + [-1]

            if self.body[move[0]][move[1]] == 0:
                self.body[move[0]][move[1]] = move[2]
            else:
                print("Incorrect move")
            self.numTurns +=1
        else:
            print("Board is already filled")

    def game(self,player1,player2):
        while not self.isFilled():
            self.turn(player1,player2)
        bestPath = self.findBestPath()
        print("Score is " + str(bestPath[0][0]) + "\n" + "best path is " + str(bestPath[0][1]))
        return bestPath[0][0]
