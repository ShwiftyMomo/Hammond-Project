#Import game board and player class
from Board import Board
from Player import Player

#Function to play a a game between player1 and player2 on a size n board
def main(player1,player2,n = 15):
    #Create the board the game will be played on
    testBoard = Board(n)
    #Play the game using the built in Board method
    return testBoard.game(player1,player2)

#Define the strategy that both players will use
#It finds the first empty spot (i.e place with a 0) and chooses that square
def minI_Strategy(body):
    #Go through all the spots
    for i in range(len(body)):
        for j in range(len(body[i])):
            #Return the first place with body[i][j]=0 when found
            if body[i][j] == 0:
                return [i,j]
    #If we get here, the board is filled with just 1s and so there is no move
    print("no valid move found")

#Create our players, and give them the strategy defined above
player1 = Player(minI_Strategy)
player2 = Player(minI_Strategy)

#Play 40 games, keeping track of the total points player1 obtains throughout
avgScore = 0
numGames = 40
for i in range(numGames):
    avgScore += main(player1,player2,40)
avgScore /= numGames
#Print the average score found
print(avgScore)